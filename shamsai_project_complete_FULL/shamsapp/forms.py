from django import forms

class SampleForm(forms.Form):
    name = forms.CharField(max_length=100)
