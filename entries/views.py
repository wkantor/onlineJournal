from django.shortcuts import render, redirect
import sys
from itertools import chain
from .models import Entry
from .forms import EntryForm
from .models import Question
from .models import Quote
from .models import Rumi
from .models import Mooji

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
    
    questions = Question.objects.all()
    quotes = Quote.objects.all()
    #rumi = Rumi.objects.all()
    #rumi.append(Mooji.objects.all())
    rumi = list(chain(Rumi.objects.all(), Mooji.objects.all()))
    
    context = {'form' : form, 'questions': questions, 'quotes': quotes,
               'rumi': rumi}
    
    return context



def index(request):
    context = common(request)
    return render(request, 'entries/index.html', context)

def free_writing(request):
    context = common(request)
    return render(request, 'entries/free_writing.html', context)

def dynamic_question(request, my_id):
    obj = Question.objects.get(id=my_id)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    return render(request, 'entries/questions.html', context)

def dynamic_quotes(request, text):
    obj = Quote.objects.get(text=text)
    context = {'object': obj}
    context1 = common(request)
    context.update(context1)
    def str_to_class(str):
        return getattr(sys.modules[__name__], str)
    return render(request, 'entries/quotes.html', context, str_to_class)
