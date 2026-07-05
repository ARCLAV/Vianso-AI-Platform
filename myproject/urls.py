"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
URL configuration for myproject project.
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    

    # Home Page
    path('index/', views.index, name='index'),

    # AI Features
    path('speech-to-text/', views.speech_to_text, name='speech_to_text'),
    path('text-to-speech/', views.text_to_speech, name='text_to_speech'),
    path('image-generation/', views.image_analyzer, name='image_analyzer'),
    path('settings/', views.settings_view, name='settings'),
    path('about/', views.about_view, name='about'),
    path('ai-assistant/', views.ai_assistant, name='ai_assistant'),
]

# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )