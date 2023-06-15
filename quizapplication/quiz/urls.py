from django.urls import path
from . import views


app_name = 'quiz'

urlpatterns = [
    path('create_quiz_category/', views.create_quiz_category, name='create_quiz_category'),
    path('add_quiz_question/', views.add_quiz_question, name='add_quiz_question'),
    path('show_quiz_question/', views.show_quiz_question, name='show_quiz_question'),
    path('quiz_index/', views.quiz_index, name='quiz_index'),
    path('delete_quiz_question/<int:question_id>/', views.delete_quiz_question, name='delete_quiz_question'),
    path('update_quiz_category/<int:category_id>/', views.update_quiz_category, name='update_quiz_category'),
    path('show_quiz_category/', views.show_quiz_category, name='show_quiz_category'),
    path('delete_quiz_category/<int:category_id>', views.delete_quiz_category, name='delete_quiz_category'),
    path('add_answer_to_questions/<int:question_id>/', views.add_answer_to_questions, name='add_answer_to_questions')
    
    
    
]
