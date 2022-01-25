from django.urls import path
from core import views

urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>/', views.NoteDetail.as_view()),
]