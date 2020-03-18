from django.shortcuts import render, redirect
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
    return render(request, 'entries/index.html', context)

def free_writing(request):
    context = common(request)
    return render(request, 'entries/free_writing.html', context)

def about(request):
    context = common(request)
    return render(request, 'entries/about.html', context)

def history(request):
    context = common(request)
    return render(request, 'entries/history.html', context)

def dynamic_question(request, my_id):
    obj = Question.objects.get(id=my_id)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/questions.html', context)

def quotes(request, text):
    obj = Quote.objects.get(text=text)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/quotes.html', context)

def quotes_sp(request,text ,id):
    obj = Quote.objects.get(text=text)
    num = obj.quote_item_set.get(id=id)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/quotes_sp.html', context)

def topics(request, text):
    obj = Topic.objects.get(text=text)
    context = {'object': obj, }
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/topics.html', context)

def topics_sp(request,text, id):
    obj = Topic.objects.get(text=text)
    num = obj.topic_item_set.get(id=id)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/topics_sp.html', context)
    
def shadows(request, text):
    obj = Shadow.objects.get(text=text)
    context = {'object': obj, }
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/shadows.html', context)

def shadows_sp(request,text, id):
    obj = Shadow.objects.get(text=text)
    num = obj.shadow_item_set.get(id=id)
    context= {'number': num, 'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/shadows_sp.html', context)
    