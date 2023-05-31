from django.contrib import admin
from .models import Question, QuizCategory, Answer


admin.site.register(Question)
admin.site.register(QuizCategory)
admin.site.register(Answer)


