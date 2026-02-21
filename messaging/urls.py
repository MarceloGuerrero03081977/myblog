from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox_view, name='inbox'),
    path('enviar/', views.send_message_view, name='send_message'),
    path('enviar/<str:username>/', views.send_message_view, name='send_message_to'),
    path('<int:pk>/', views.message_detail_view, name='message_detail'),
    path('<int:pk>/eliminar/', views.delete_message_view, name='delete_message'),
]