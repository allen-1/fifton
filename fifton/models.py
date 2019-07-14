from django.contrib.auth.models import User 
from django.db import models

class UserInfo(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128) 
	phone_no = models.CharField(max_length=12)
	def __str__(self):
		return self.name 

class filmacad(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128) 
	phone_no = models.CharField(max_length=12)
	def __str__(self):
		return self.name 

class musicacad(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128) 
	phone_no = models.CharField(max_length=12)
	def __str__(self):
		return self.name 


class photoacad(models.Model):
	name = models.CharField(max_length=128)
	email = models.CharField(max_length=128) 
	phone_no = models.CharField(max_length=12)
	def __str__(self):
		return self.name 
