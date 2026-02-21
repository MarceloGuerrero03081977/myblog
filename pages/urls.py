from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageListView.as_view(), name='page_list'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='page_detail'),
    path('crear/', views.PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/editar/', views.PageUpdateView.as_view(), name='page_update'),
    path('<int:pk>/eliminar/', views.PageDeleteView.as_view(), name='page_delete'),
]