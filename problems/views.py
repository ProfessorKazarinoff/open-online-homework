# problems/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Problem

class ProblemListView(ListView):
    model = Problem
    template_name = 'problem_list.html'

class ProblemCreateView(CreateView):
    model = Problem
    fields = (
        'title',
        'question',
        'answer_one',
        'answer_two',
        'answer_three',
        'answer_four',
        'correct_answer',
        'assignment',
        'author')
    template_name = 'problem_new.html'

class ProblemDetailView(DetailView):
    model = Problem
    template_name = 'problem_detail.html'

class ProblemUpdateView(UpdateView):
    model = Problem
    fields = (
        'title',
        'question',
        'answer_one',
        'answer_two',
        'answer_three',
        'answer_four',
        'correct_answer',
        'assignment',
        'author')
    template_name = 'problem_edit.html'

class ProblemDeleteView(DeleteView):
    model = Problem
    template_name = 'problem_delete.html'
    success_url = reverse_lazy('problem_list')
