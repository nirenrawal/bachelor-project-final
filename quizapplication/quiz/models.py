from django.db import models



class QuizCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "quiz catogeries"
    
    def __str__(self):
        return self.name


class Question(models.Model):
    content = models.CharField(max_length=255)
    quiz_subject = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    number_of_questions = models.IntegerField(default=1)
    time = models.IntegerField(help_text="Duration in Seconds", default=1)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.answer_set.all()
    
    
class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Question: {self.question.content}, answer: {self.content}, Correct Answer: {self.correct_answer}"