import urllib
import json

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import sys
from itertools import chain
from .models import Entry
from .forms import EntryForm
from .models import Question
from .models import Plunge
from .models import Quote
from .models import Quote_item
from .models import Topic
from .models import Topic_item
from .models import Shadow
from .models import Shadow_item

# once we hit a url, it asks here, views, what to show the user
# "redner" displays a template, takes in (request [same as up in definition], and the template)

def entry(request, topic):
    if request.method == 'POST':
        # this means, if they hit save
        form = EntryForm(request.POST)
        text = request.POST.get('text')
        topic = topic
        if form.is_valid():
            if request.user.is_authenticated:
                post_save = Entry(text=text, author=request.user, topic=topic)
                post_save.save()
                #form.save()
            else:
                messages.info(request, 'You need to be logged in for this!')
    else:
        form = EntryForm()
    

def common(request):
    form = EntryForm() 
    topics = Topic.objects.all()
    questions = Question.objects.all()
    quotes = Quote.objects.all()
    shadows = Shadow.objects.all()
    plunges = Plunge.objects.all()
    
    context = {'form' : form, 'questions': questions, 'quotes': quotes,
               'topics': topics, 'shadows': shadows, 'plunges': plunges }
    
    return context



def index(request):
    context = common(request)
    return render(request, 'main/index.html', context)

def free_writing(request):
    topic = "Free Writing"
    entry(request, topic)
    context = common(request)
    return render(request, 'main/free_writing.html', context)

def about(request):
    context = common(request)
    return render(request, 'main/about.html', context)

def privacy_policy(request):
    context = common(request)
    return render(request, 'main/privacy_policy.html', context)

def about_plunge(request):
    context = common(request)
    return render(request, 'plunges/about_plunge.html', context)

def dynamic_question(request, my_id):
    obj = Question.objects.get(id=my_id)
    topic = obj
    entry(request, topic)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/questions.html', context)

def plunge1(request):
    context = common(request)
    return render(request, 'plunges/plunge1.html', context)

def plunge2(request):
    context = common(request)
    return render(request, 'plunges/plunge2.html', context)

def plunge3(request):
    context = common(request)
    return render(request, 'plunges/plunge3.html', context)

def plunge_sp1(request, id):
    obj = Plunge.objects.get(id=id)
    context= {'object': obj,}
    context1 = common(request)
    context.update(context1)
    return render(request, 'plunges/plunge_sp1.html', context)

def plunge_sp2(request, id):
    obj = Plunge.objects.get(id=id)
    context= {'object': obj,}
    context1 = common(request)
    context.update(context1)
    return render(request, 'plunges/plunge_sp2.html', context)

def plunge_sp3(request, id):
    obj = Plunge.objects.get(id=id)
    context= {'object': obj,}
    context1 = common(request)
    context.update(context1)
    return render(request, 'plunges/plunge_sp3.html', context)

def quotes(request, text):
    obj = Quote.objects.get(text=text)
    topic = obj
    entry(request, topic)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/quotes.html', context)

def quotes_sp(request,text ,id):
    obj = Quote.objects.get(text=text)
    num = obj.quote_item_set.get(id=id)
    topic = num
    entry(request, topic)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/quotes_sp.html', context)

def topics(request, text):
    obj = Topic.objects.get(text=text)
    topic = obj
    entry(request, topic)
    context = {'object': obj, }
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/topics.html', context)

def topics_sp(request,text, id):
    obj = Topic.objects.get(text=text)
    num = obj.topic_item_set.get(id=id)
    topic = num
    entry(request, topic)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/topics_sp.html', context)
    
def shadows(request, text):
    obj = Shadow.objects.get(text=text)
    topic = obj
    entry(request, topic)
    context = {'object': obj, }
    context1 = common(request)
    context.update(context1)
    return render(request, 'menus/shadows.html', context)

def shadows_sp(request,text, id):
    obj = Shadow.objects.get(text=text)
    num = obj.shadow_item_set.get(id=id)
    topic = num
    entry(request, topic)
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
                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())
                ''' End reCAPTCHA validation '''
    
                if result['success']:
                    
                    user = User.objects.create_user(username=username, password=password1)
                    user.save
                    messages.info(request, "Account created.")
                    return redirect('register_complete')
                else:
                    messages.info(request, 'Invalid reCAPTCHA. Please try again.')
                    return redirect('register')
        else:
            messages.info(request, "Passwords not matching.")
            return redirect('register')
        
    else:
        return render(request, 'accounts/register.html', context)
    
def register_complete(request):
    context = common(request)
    return render(request, 'accounts/register_complete.html', context)

def login(request):
    context = common(request)
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong username or password.')
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html', context)     
    
def logout(request):
    auth.logout(request)
    return redirect('home')

def history(request):
    ent = Entry.objects.filter(author=request.user)
    ent = ent.order_by('-date')
    context={'entries': ent}
    context1 = common(request)
    context.update(context1)
    return render(request, 'main/history.html', context)