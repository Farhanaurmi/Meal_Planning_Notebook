from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default="unnamed.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
		return self.name