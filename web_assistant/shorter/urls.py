from django.urls import path, include
from .views import shorter, to_source_url, delete_link

urlpatterns = [
    path('', shorter, name='shorter'),
    path('delete/<str:url_id>/', delete_link, name='delete'),
    # path('<str:url_id>/', to_source_url, name='to_source_url'),
]
