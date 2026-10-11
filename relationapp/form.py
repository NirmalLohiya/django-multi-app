from django import forms
from .models import *


class blogForm(forms.ModelForm):
   class Meta:
      model=Blog
      field='__all__'
    #   field=['title','description','image']

