from django import forms


class GeneratorForm(forms.Form):
    pws_lenght = forms.IntegerField(min_value=4, max_value=256)
    letters = forms.BooleanField(required=False)
    numbers = forms.BooleanField(required=False)
    spec_chars = forms.BooleanField(required=False)