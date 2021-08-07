from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):

    class Meta():
        model = Diary
        fields = ('id','Title','Date','Text',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['Text'].widget.attrs.update({'class':'textarea','placeholder':"What you do today..."})
        self.fields['Title'].widget.attrs.update({'class':'textinput','placeholder':"Enter title..."})
