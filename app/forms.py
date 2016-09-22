from django import forms

class search(forms.Form):
    vaule = forms.CharField(label="search",max_length=100)


