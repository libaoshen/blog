from django import forms


class QueryForm(forms.Form):
    message = forms.CharField()