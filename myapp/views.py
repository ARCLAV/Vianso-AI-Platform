from django.shortcuts import render, redirect
from dotenv import load_dotenv
from groq import Groq
from pathlib import Path
import os
from gtts import gTTS
from langdetect import detect
import uuid
from django.conf import settings
import urllib.parse
import base64
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required


# Load .env
env_path = Path(__file__).resolve().parent.parent / "myproject" / ".env"
load_dotenv(env_path)

print("ENV PATH =", env_path)
print("GROQ 1 =", os.getenv("GROQ_API_KEY_1"))
print("GROQ 2 =", os.getenv("GROQ_API_KEY_2"))
print("GROQ 3 =", os.getenv("GROQ_API_KEY_3"))

groq_client_1 = Groq(
    api_key=os.getenv("GROQ_API_KEY_1")
)

groq_client_2 = Groq(
    api_key=os.getenv("GROQ_API_KEY_2")
)

groq_client_3 = Groq(
    api_key=os.getenv("GROQ_API_KEY_3")
)



def settings_view(request):
    return render(request, "settings.html")
def about_view(request):
    return render(request, "about.html")
def ai_assistant(request):

    response_text = ""

    if request.method == "POST":

        prompt = request.POST.get("prompt")

        response = groq_client_3.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        response_text = (
            response
            .choices[0]
            .message
            .content
        )

    return render(
        request,
        "ai_assistant.html",
        {
            "response":response_text
        }
    )

def login(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("index")
        else:
            error = "Invalid username or password"

    return render(request, "login.html", {"error": error})


def register(request):
    error = ""
    success = ""

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            error = "Passwords do not match"

        elif User.objects.filter(username=username).exists():
            error = "Username already exists"

        elif User.objects.filter(email=email).exists():
            error = "Email already exists"

        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            success = "Account created successfully. Please login."

    return render(request, "register.html", {
        "error": error,
        "success": success
    })


@login_required(login_url="login")


def index(request):
    return render(request, 'index.html')


def speech_to_text(request):
    upload_transcript = ""
    live_transcript = ""
    error = ""

    if request.method == "POST":

        source = request.POST.get("source")

        if "audio" in request.FILES:

            audio_file = request.FILES["audio"]

            if audio_file.size > 20 * 1024 * 1024:
                error = "Audio file too large. Please upload below 20 MB."

            else:
                selected_language = request.POST.get("language")

                if selected_language == "auto":
                    selected_language = None

                transcription = groq_client_1.audio.transcriptions.create(
                file=(audio_file.name, audio_file.read()),
                model="whisper-large-v3",
                response_format="text",
                language=selected_language
                )
               
                final_text = transcription

                if selected_language == "ml":
                    chat = groq_client_1.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "system",
                                "content": "Convert the given text into Malayalam script only. Do not explain. Do not translate to English."
                            },
                            {
                                "role": "user",
                                "content": final_text
                            }
                        ]
                    )

                    final_text = chat.choices[0].message.content

                if source == "upload":
                    upload_transcript = final_text

                elif source == "live":
                    live_transcript = final_text

    return render(request, "speech_to_text.html", {
        "upload_transcript": upload_transcript,
        "live_transcript": live_transcript,
        "error": error
    })


def text_to_speech(request):
    audio_file = None

    if request.method == "POST":

        text = request.POST.get("text", "").strip()
        voice = request.POST.get("voice", "autumn")

        if text:

            audio_folder = os.path.join(
                settings.MEDIA_ROOT,
                "audio"
            )

            os.makedirs(audio_folder, exist_ok=True)

            try:

                language = detect(text)

                gtts_languages = [
                    "ml",  # Malayalam
                    "hi",  # Hindi
                    "ta",  # Tamil
                    "te",  # Telugu
                    "kn",  # Kannada
                    "bn",  # Bengali
                    "mr",  # Marathi
                    "gu",  # Gujarati
                    "pa",  # Punjabi
                    "ur",  # Urdu
                    "fr",  # French
                    "de",  # German
                    "es",  # Spanish
                    "ja",  # Japanese
                    "ko",  # Korean
                    "zh"   # Chinese
                ]

                # Use gTTS for supported languages
                if language in gtts_languages:

                    if language == "zh":
                        language = "zh-cn"

                    filename = f"{uuid.uuid4()}.mp3"

                    filepath = os.path.join(
                        audio_folder,
                        filename
                    )

                    tts = gTTS(
                        text=text,
                        lang=language,
                        slow=False
                    )

                    tts.save(filepath)

                # Use Groq for English
                else:

                    filename = f"{uuid.uuid4()}.wav"

                    filepath = os.path.join(
                        audio_folder,
                        filename
                    )

                    response = groq_client_2.audio.speech.create(
                        model="canopylabs/orpheus-v1-english",
                        voice=voice,
                        input=text,
                        response_format="wav"
                    )

                    response.write_to_file(filepath)

                audio_file = (
                    settings.MEDIA_URL +
                    "audio/" +
                    filename
                )

            except Exception as e:
                print("Error:", str(e))

    return render(
        request,"text_to_speech.html",
        {
            "audio_file": audio_file}
    )


from django.core.files.storage import FileSystemStorage
def image_analyzer(request):

    result = None
    uploaded_image = None

    if request.method == "POST":

        image = request.FILES.get("image")

        language = request.POST.get(
            "language",
            "English"
        )

        print("Selected Language =", language)

        if image:

            fs = FileSystemStorage()

            filename = fs.save(
                image.name,
                image
            )

            uploaded_image = fs.url(
                filename
            )

            image.seek(0)

            image_bytes = image.read()

            base64_image = base64.b64encode(
                image_bytes
            ).decode("utf-8")

            prompt = f"""
Analyze this image in detail.

Describe:
- Objects
- People
- Scene
- Colors
- Text present in image

IMPORTANT:
Respond completely in {language}.

Do not use English unless the selected language is English.

Translate all extracted text and descriptions into {language}.
"""

            response = groq_client_3.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ]
            )

            result = (
                response
                .choices[0]
                .message
                .content
            )

    return render(
        request,
        "image_analyzer.html",
        {
            "result": result,
            "uploaded_image": uploaded_image
        }
    )

