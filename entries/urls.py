
from django.urls import path
from . import views

# . means current module - entries (the folder we are in)

urlpatterns = [
    
    
    path('', views.index, name= 'home'),
    path('free_writing', views.free_writing, name= 'free_writing'),
    path('about', views.about, name= 'about'),
    path('history', views.history, name= 'history'),
    path('questions/<int:my_id>/', views.dynamic_question, name= 'questions'),
    
    path('quotes/<str:text>/', views.quotes, name= 'quotes'),
    path('quotes/<str:text>/<int:id>', views.quotes_sp, name= 'quotes_sp'),
    
    path('topics/<str:text>/', views.topics, name= 'topics'),
    path('topics/<str:text>/<int:id>', views.topics_sp, name= 'topics_sp'),
    
    path('shadows/<str:text>/', views.shadows, name= 'shadows'),
    path('shadows/<str:text>/<int:id>', views.shadows_sp, name= 'shadows_sp'),
    
    path('register', views.register, name= 'register'),
    path('register_complete', views.register_complete, name= 'register_complete'),
    

]
# when user lands on '' (nothing), it sends him to views.index