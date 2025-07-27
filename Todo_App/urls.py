from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('addtask/', addtask, name='addtask'),
    path('marks_as_done/<int:pk>/',marks_as_done, name='marks_as_done'),
    path('marks_as_undone/<int:pk>/',marks_as_undone, name='marks_as_undone'),
    path('edit/<int:pk>/', edittask, name='edittask'),
    path('delete/<int:pk>/', deletetask, name='deletetask'),
]