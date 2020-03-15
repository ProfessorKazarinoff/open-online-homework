# problems/urls.py

from django.urls import path

from .views import ProblemListView, ProblemCreateView, ProblemUpdateView, ProblemDetailView, ProblemDeleteView

urlpatterns = [
    path('<int:pk>/edit', ProblemUpdateView.as_view(), name='problem_edit'),
    path('<int:pk>/delete', ProblemDeleteView.as_view(), name='problem_delete'),
    path('<int:pk>', ProblemDetailView.as_view(), name='problem_detail'),
    path('new/', ProblemCreateView.as_view(), name='problem_new'),
    path('', ProblemListView.as_view(), name='problem_list'),
]
