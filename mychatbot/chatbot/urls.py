from django.urls import path
from .views import get_question

urlpatterns = [
    path('api/question/', get_question, name='get_question'),
]