from django.shortcuts import render, redirect
from .form import QuizCategoryForm, QuestionForm
from django.contrib.auth.decorators import login_required
from .models import Question, QuizCategory
from django.contrib import messages


@login_required
def quiz_index(request):
    return render(request, "quiz/quiz_index.html")

""" This function creates quiz category """

@login_required
def create_quiz_category(request):
    if request.method == 'POST':
        form = QuizCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['name']
            if not QuizCategory.objects.filter(name=category_name).exists():
                form.save()
                messages.success(request, "Your Quiz Category Has Been Created.")
                return redirect('quiz:quiz_index')
            else:
                messages.error(request, "The Quiz Category Already Exists.")
        else:
            messages.error(request, "Your Form Data Is Invalid.")
    else:
        form = QuizCategoryForm()
    return render(request, 'quiz/create_quiz_category.html', {'form': form})






""" This function adds quizes in database """
@login_required
def add_quiz_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                form = QuestionForm()
                messages.success(request, "Your quiz question has been added successfully.")
            except ValueError as e:
                error_msg = str(e)
                messages.error(request, error_msg)
    else:
        form = QuestionForm()
    return render(request, "quiz/add_quiz_question.html", {'form':form}) 


def show_quiz_question(request):
    questions = Question.objects.all()
    return render(request, "quiz/show_quiz_question.html", {'questions':questions})


""" This function deletes the quiz questions """
@login_required
def delete_quiz_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        question.delete()
        messages.success(request, "The quiz question has been deleted successfully.")
    except Question.DoesNotExist:
        messages.error(request, "The quiz question does not exist.")
    return redirect('quiz:show_quiz_question')
    


