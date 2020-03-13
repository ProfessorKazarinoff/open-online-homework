from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.code} {self.title}'

class Section(models.Model):
    CRN = models.IntegerField(unique=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.CRN)
