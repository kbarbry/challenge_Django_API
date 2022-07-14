from django.db import models

class Form(models.Model):
	name = models.CharField(max_length=40, unique=True, default="name")
	description = models.CharField(max_length=512, default="description")

	def __str__(self):
		return self.name

class Item(models.Model):
	form = models.ForeignKey(Form, on_delete=models.CASCADE)

	photo = models.CharField(max_length=1024, default="")
	description = models.CharField(max_length=512, default="description")
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.description

class People(models.Model):
	name = models.CharField(max_length=20, unique=True)
	username = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name