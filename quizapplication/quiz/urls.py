from django.urls import path
from . import views


urlpatterns = [
    path('create_quiz_category/', views.create_quiz_category, name='create_quiz_category')
]
