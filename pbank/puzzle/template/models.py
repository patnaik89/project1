from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Categories(models.Model):
    categories_text = models.CharField(max_length=100)

    def __str__(self):
        return self.categories_text

class Question(models.Model):
    question_text = models.TextField(default=None)
    tittle = models.CharField(max_length=200)
    category_relation = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    answer_text =models.TextField(default=None)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    def _str_(self):
        return self.answer_text

class Comment (models.Model):
    comment_text =models.TextField(default=None)
    answer =models.ForeignKey(Answer,on_delete=models.CASCADE)
    def _str_(self):
        return self.answer_text


