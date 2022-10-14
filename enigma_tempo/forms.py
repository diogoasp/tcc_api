from dataclasses import field
from django import forms
from .models import *

class CardForm(forms.ModelForm):
  class Meta:
    model = Card
    fields = '__all__'

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      for visible in self.visible_fields():
          visible.field.widget.attrs['class'] = 'form-control'