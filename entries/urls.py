
from django.urls import path, include
from . import views
from django.contrib import admin
# . means current module - entries (the folder we are in)

urlpatterns = [
    
   # path('', include("django.contrib.auth.urls")),
    
    path('', views.index, name= 'home'),
    path('free_writing', views.free_writing, name= 'free_writing'),
    path('about', views.about, name= 'about'),
    path('questions/<int:my_id>/', views.dynamic_question, name= 'questions'),
    path('quotes/<str:text>/', views.dynamic_quotes, name= 'quotes'),
    path('quotes/<str:text>/<int:q_id>', views.quotes_sp, name= 'quotes_sp'),
    path('topics/<str:text>/', views.topics, name= 'topics'),
    path('topics/<str:text>/<int:id>', views.topics_sp, name= 'topics_sp'),
    

]
# when user lands on '' (nothing), it sends him to views.index