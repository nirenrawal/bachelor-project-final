from django.shortcuts import render
from .form import QuizCategoryForm, QuestionForm
from django.contrib.auth.decorators import login_required


@login_required
def quiz_index(request):
    return render(request, "quiz/quiz_index.html")

""" This function creates quiz category """
def create_quiz_category(request):
    if request.method == "POST":
        form = QuizCategoryForm(request.POST)
        if form.is_valid():
            quiz_subject = form.save(commit=False)
            quiz_subject.save()
            obj = form.instance
            return render(request, 'quiz/create_quiz_category.html', {'obj': obj})
    else:
        form = QuizCategoryForm()
    return render(request, 'quiz/create_quiz_category.html', {'form': form})



""" This function adds quizes in database """
def add_quiz_question(request):
    # questions = Question.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, "quiz/add_quiz_question.html")
            except ValueError as e:
                error_msg = str(e)
                return render(request, "quiz/add_quiz_question.html", {'form': form, 'error_msg': error_msg})
    else:
        form = QuestionForm()
    return render(request, "quiz/add_quiz_question.html", {'form':form}) #'questions': questions



# def show_quiz_questions(request):
#     questions = Question.objects.all()
#     return render(request, "quiz/")





