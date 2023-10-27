from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100,widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)
