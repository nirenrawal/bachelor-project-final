from django.shortcuts import render, redirect, get_object_or_404
from .form import QuizCategoryForm, QuestionForm
from django.contrib.auth.decorators import login_required
from .models import Question, QuizCategory, Answer
from django.contrib import messages
from django.forms import inlineformset_factory, formset_factory



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


@login_required
def delete_quiz_category(request, category_id):
    try:
        category = QuizCategory.objects.get(id=category_id)
        category.delete()
        messages.success(request, "The quiz category has been deleted successfully.")
    except Question.DoesNotExist:
        messages.error(request, "The quiz category does not exist.")
    return redirect('quiz:show_quiz_category')


@login_required
def show_quiz_category(request):
    quiz_categories = QuizCategory.objects.all()
    return render(request, "quiz/show_quiz_category.html", {'quiz_categories':quiz_categories})

 
 
 

    
@login_required
def update_quiz_category(request, category_id):
    quiz_category = get_object_or_404(QuizCategory, id=category_id)
    
    if request.method == 'POST':
        form = QuizCategoryForm(request.POST, instance=quiz_category)
        if form.is_valid():
            category_name = form.cleaned_data['name']
            if not QuizCategory.objects.filter(name=category_name).exclude(id=category_id).exists():
                form.save()
                messages.success(request, "The quiz category has been updated successfully.")
                return redirect('quiz:show_quiz_category')
            else:
                messages.error(request, "The quiz category already exists.")
        else:
            messages.error(request, "The form data is invalid.")
    else:
        initial_val = {
            'name': quiz_category.name,
            'description': quiz_category.description,
            'number_of_questions': quiz_category.number_of_questions,
            'time': quiz_category.time,
        }
        form = QuizCategoryForm(instance=quiz_category, initial=initial_val)
    return render(request, "quiz/update_quiz_category.html", {'form': form})



@login_required
def add_answer_to_questions(request, question_id):
    question = Question.objects.get(id=question_id)
    question_form_set = inlineformset_factory(Question, Answer, fields=('content', 'correct_answer', 'question'), extra=4, max_num=4)
    if request.method == 'POST':
        form = question_form_set(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, "Your answers has been added successfully.")
            return redirect('quiz:show_quiz_question')
    else:
        form = question_form_set(instance=question)
    return render(request, "quiz/add_answer_to_questions.html", {'form':form, 'question':question})
    
