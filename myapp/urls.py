from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('speech-to-text/', views.speech_to_text, name='speech_to_text'),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
    path('image-generation/', views.image_analyzer, name='image_analyzer'),
    path('settings/', views.settings_view, name='settings'),
    path('about/', views.about_view, name='about'),
    path('ai-assistant/', views.ai_assistant, name='ai_assistant'),
]