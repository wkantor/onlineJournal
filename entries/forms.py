# just like the model is a python representation of the database, classes created
#   as forms are representations of the HTML forms

from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        # Meta class is just additional information to the class
        model = Entry
        fields = ('text', )
            # this is telling ModelForm - create a form from the model 'Entry', using field 'text'
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # include the default init from ModelForm, initate the original init.py + ...
        self.fields['text'].widget.attrs.update({'class': 'textarea', 'placeholder': 'Write here.'})
            # change the attributes of the widget
            # textarea is from the html
        
        