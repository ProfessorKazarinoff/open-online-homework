# problems/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from assignments.models import Assignment

class Problem(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField()
    answer_one = models.TextField()
    answer_two = models.TextField()
    answer_three = models.TextField()
    answer_four = models.TextField()
    correct_answer = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='problems')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('problem_detail', args=[str(self.id)])
