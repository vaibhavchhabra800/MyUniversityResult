from django import forms
from .models import usermodelk1


class formcheck(forms.ModelForm):
    class Meta:
        model=usermodelk1
        exclude=['id']

  #  def clean_maths(self):



