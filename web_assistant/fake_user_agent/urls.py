from django.urls import path
from .views import user_agent


urlpatterns = [
    path('', user_agent, name='user_agent'),

]

