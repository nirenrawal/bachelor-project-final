from django.urls import path
from . import views


app_name = 'quiz'

urlpatterns = [
    path('create_quiz_category/', views.create_quiz_category, name='create_quiz_category'),
    path('add_quiz_question/', views.add_quiz_question, name='add_quiz_question'),
    path('quiz_index/', views.quiz_index, name='quiz_index'),
]
