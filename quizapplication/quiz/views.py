from django.shortcuts import render
from .form import QuizCategoryForm



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
# Create your views here.
