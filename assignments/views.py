# assignments/views.py

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Assignment

class AssignmentListView(ListView):
    model = Assignment
    template_name = 'assignment_list.html'

class AssignmentCreateView(CreateView):
    model = Assignment
    fields = ('title','body','author')
    template_name = 'assignment_new.html'

class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignment_detail.html'

class AssignmentUpdateView(UpdateView):
    model = Assignment
    fields = ('title','body')
    template_name = 'assignment_edit.html'

class AssignmentDeleteView(DeleteView):
    model = Assignment
    template_name = 'assignment_delete.html'
    success_url = reverse_lazy('assignment_list')
