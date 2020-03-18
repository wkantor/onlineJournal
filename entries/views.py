from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import sys
from itertools import chain
from .models import Entry
from .forms import EntryForm
from .models import Question
from .models import Quote
from .models import Quote_item
from .models import Topic
from .models import Topic_item
from .models import Shadow
from .models import Shadow_item

# once we hit a url, it asks here, views, what to show the user
# "redner" displays a template, takes in (request [same as up in definition], and the template)

def common(request):
    if request.method == 'POST':
        # this means, if they hit save
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EntryForm()
    form = EntryForm()
    
    topics = Topic.objects.all()
    questions = Question.objects.all()
    quotes = Quote.objects.all()
    shadows = Shadow.objects.all()
    
    context = {'form' : form, 'questions': questions, 'quotes': quotes,
               'topics': topics, 'shadows': shadows }
    
    return context



def index(request):
    context = common(request)
    return render(request, 'main/index.html', context)

def free_writing(request):
    context = common(request)
    return render(request, 'main/free_writing.html', context)

def about(request):
    context = common(request)
    return render(request, 'main/about.html', context)

def history(request):
    context = common(request)
    return render(request, 'main/history.html', context)

def dynamic_question(request, my_id):
    obj = Question.objects.get(id=my_id)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/questions.html', context)

def quotes(request, text):
    obj = Quote.objects.get(text=text)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/quotes.html', context)

def quotes_sp(request,text ,id):
    obj = Quote.objects.get(text=text)
    num = obj.quote_item_set.get(id=id)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/quotes_sp.html', context)

def topics(request, text):
    obj = Topic.objects.get(text=text)
    context = {'object': obj, }
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/topics.html', context)

def topics_sp(request,text, id):
    obj = Topic.objects.get(text=text)
    num = obj.topic_item_set.get(id=id)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/topics_sp.html', context)
    
def shadows(request, text):
    obj = Shadow.objects.get(text=text)
    context = {'object': obj, }
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/shadows.html', context)

def shadows_sp(request,text, id):
    obj = Shadow.objects.get(text=text)
    num = obj.shadow_item_set.get(id=id)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/shadows_sp.html', context)

def register(request):
    context = common(request)
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1)
                user.save
                messages.info(request, "Account created.")
                return redirect('register_complete')
        else:
            messages.info(request, "Passwords not matching.")
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html', context)
    
def register_complete(request):
    context = common(request)
    return render(request, 'accounts/register_complete.html', context)
