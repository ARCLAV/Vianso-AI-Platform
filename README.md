# 🤖 Vianso AI

Vianso AI is a Django-based AI assistant platform that integrates multiple AI-powered utilities into a single web application. It provides features such as Speech-to-Text, Text-to-Speech, Image Generation, Image Analysis, and an AI Chat Assistant through an intuitive and modern user interface.

---

## 🚀 Features

- 🎙️ Speech-to-Text
  - Convert spoken audio into text.
  - Fast and accurate speech recognition.

- 🔊 Text-to-Speech
  - Convert text into natural-sounding speech.
  - Supports multiple languages and voices.

- 🖼️ Image Generation
  - Generate AI-powered images from text prompts.

- 🔍 Image Analysis
  - Upload images and receive AI-generated descriptions and insights.

- 💬 AI Chat Assistant
  - Intelligent chatbot for answering questions and assisting users.

- 🎨 Modern User Interface
  - Responsive dashboard
  - Clean and user-friendly design
  - Easy navigation between AI tools

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### Backend
- Python
- Django

### AI Services
- Groq API
- xAI API

### Database
- SQLite3

---

## 📁 Project Structure

```
Vianso-AI/
│
├── media/
├── myapp/
│   ├── templates/
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/ARCLAV/Vianso-AI-Platform.git
cd Vianso-AI-Platform
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file inside the `myproject` folder.

```env
XAI_API_KEY=your_xai_api_key
KEY_1=your_groq_api_key
KEY_2=your_second_groq_api_key
SECRET_KEY=your_django_secret_key
```

---

## ▶️ Run the Project

Apply migrations

```bash
python manage.py migrate
```

Start the development server

```bash
python manage.py runserver
```

Open your browser and visit

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

You can add screenshots here.

```
Home Dashboard
Speech to Text
Text to Speech
Image Generation
Image Analysis
AI Chat Assistant
```

---

## 🔮 Future Enhancements

- Voice-based AI assistant
- User authentication
- Conversation history
- PDF summarization
- Document analysis
- AI coding assistant
- Cloud deployment
- Multi-language support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Developer

**Sooraj G Menon**

B.Tech Information Technology

TOCH Institute of Science and Technology

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
