# src/assignments/urls.py

from django.urls import path

from .views import AssignmentListView, AssignmentCreateView, AssignmentUpdateView, AssignmentDetailView, AssignmentDeleteView

urlpatterns = [
    path('<int:pk>/edit', AssignmentUpdateView.as_view(), name='assignment_edit'),
    path('<int:pk>/delete', AssignmentDeleteView.as_view(), name='assignment_delete'),
    path('<int:pk>', AssignmentDetailView.as_view(), name='assignment_detail'),
    path('new/', AssignmentCreateView.as_view(), name='assignment_new'),
    path('', AssignmentListView.as_view(), name='assignment_list'),
]
