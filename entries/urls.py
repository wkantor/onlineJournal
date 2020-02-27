
from django.urls import path
from . import views
# . means current module - entries (the folder we are in)

urlpatterns = [
    path('', views.index, name= 'home'),
    path('free_writing', views.free_writing, name= 'free_writing'),
    path('questions/<int:my_id>/', views.dynamic_question, name= 'questions'),
    path('quotes/<str:text>/', views.dynamic_quotes, name= 'quotes')

]
# when user lands on '' (nothing), it sends him to views.index