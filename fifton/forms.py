from django import forms 
from django.contrib.auth.models import User 
from fifton.models import UserInfo, filmacad, musicacad, photoacad

class UserInfoForms(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text='please enter name')
	email = forms.EmailField(help_text='please enter  email')
	phone_no = forms.CharField(max_length=12,help_text='Phone No.' )

	class Meta:
		model = UserInfo
		fields = ('name', 'email', 'phone_no')

class filmacadForms(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text='please enter name')
	email = forms.EmailField(help_text='please enter  email')
	phone_no = forms.CharField(max_length=12,help_text='Phone No.' )

	class Meta:
		model = filmacad
		fields = ('name', 'email', 'phone_no')

class musicacadForms(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text='please enter name')
	email = forms.EmailField(help_text='please enter  email')
	phone_no = forms.CharField(max_length=12,help_text='Phone No.' )

	class Meta:
		model = musicacad
		fields = ('name', 'email', 'phone_no')

class photoacadForms(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text='please enter name')
	email = forms.EmailField(help_text='please enter  email')
	phone_no = forms.CharField(max_length=12,help_text='Phone No.' )

	class Meta:
		model = photoacad
		fields = ('name', 'email', 'phone_no')