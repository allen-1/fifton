import smtplib, ssl 
from django.shortcuts import render
from django.http import HttpResponse 
from fifton.forms import UserInfoForms, filmacadForms, musicacadForms, photoacadForms

sender_email = "allenagozie@gmail.com"
receiver_email = "ericamettaz@gmail.com"
message = """\
Subject: PY test.


Did you receive this?

"""

port = 465 
password = input("type your password and press enter: ")
context = ssl.create_default_context()

def index(request):
	context_dict = {'message': "Film, Music, Art..."}
	return render(request, 'temp/home.html', context=context_dict)

def about(request):
	return render(request, 'temp/about.html', context={})

def add_userinfo(request):
	form = UserInfoForms()
	if request.method == 'POST':
		form = UserInfoForms(request.POST)
		if form.is_valid():
			form.save(commit=True)
			with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
				server.login("allenagozie@gmail.com", password)
				server.sendmail(sender_email, receiver_email, message)
			return index(request)
		else:
			print(form.errors)
	return render(request, 'fifton/add_userinfo.html', {'form':form})

def filmacad(request):
	form = filmacadForms()
	if request.method == 'POST':
		form = filmacadForms(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return filmacad(request)
		else:
			print(form.errors)
	return render(request, 'fifton/filmacad.html', {'form':form})

def musicacad(request):
	form = musicacadForms()
	if request.method == 'POST':
		form = musicacadForms(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return musicacad(request)
		else:
			print(form.errors)
	return render(request, 'fifton/musicacad.html', {'form':form})

def photoacad(request):
	form = photoacadForms()
	if request.method == 'POST':
		form = photoacadForms(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return photoacad(request)
		else:
			print(form.errors)
	return render(request, 'fifton/photoacad', {'form':form})