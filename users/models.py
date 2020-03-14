# users/models.py

from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

PERMISSION_LEVEL_CHOICES = (
    ('Super User', 'SuperUser'),
	('Admin', 'Admin'),
	('Instructor', 'Instructor'),
	('Teachering Assistant', 'TeachingAssistant'),
	('Student', 'Student'),
	('Observer', 'Observer'),
)

PERMISSION_LEVEL_SORT_ORDER = dict([(level[1], index) for index, level in enumerate(PERMISSION_LEVEL_CHOICES)])

def compare_permissions(one, another):
    return PERMISSION_LEVEL_SORT_ORDER[another] - PERMISSION_LEVEL_SORT_ORDER[one]



class User(AbstractUser):
    email = models.CharField(max_length=30, blank=False)
    id_number = models.CharField(max_length=30, blank=True, null=True)
    institution = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.email
