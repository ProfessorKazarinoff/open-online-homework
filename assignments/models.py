# assignments/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    available_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assignment_detail', args=[str(self.id)])
