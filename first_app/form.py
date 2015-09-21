from django import forms

class Userform(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

class Fileform(forms.Form):
	file = forms.FileField()
