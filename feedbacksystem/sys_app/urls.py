"""
URL configuration for feedbacksystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')).
"""

from django.urls import path
from sys_app import views




urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('python/', views.python, name='python'),
    path('courses/', views.course, name='courses'),
    path('java/', views.java, name='java'),
    path('moduler/', views.moduler, name='moduler'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('feedback/', views.feedback, name='feedback'),
    path('reviews/', views.showfeedback, name='reviews'),
    path('signout/', views.signout, name='signout'),
]
