from django import forms

class CreateForm(forms.Form):
	name = forms.CharField(label='Name', max_length=40)
	description = forms.CharField(label='Description', max_length=512)
	check = forms.BooleanField(required=False)