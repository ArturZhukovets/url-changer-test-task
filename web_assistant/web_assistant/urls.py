"""web_assistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import home, register, user_login, user_logout
from shorter.views import to_source_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('shorter/', include('shorter.urls')),
    path('user-agent/', include('fake_user_agent.urls')),
    path('<str:url_id>/', to_source_url, name='to_source_url'),   # if user copy short url and use it without href link.

]
