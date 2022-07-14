# 🐍 Django 24h Challenge 🐍

## Commands to start

django-admin startproject \<nameProject\> *create a new project*</br>
python3 manage.py runserver 8000 *run the server in 127.0.0.1/8000*</br>
python3 manage.py startapp \<nameApp\></br>

## When you want to config your app

adding a function with a render in your nameApp.views</br>
```
from django.shortcuts import render
from django.http import HttpResponse

def mainPage(response):
	return HttpResponse("<h1>Welcome to our site</h1>")
```

adding a urls.py file to the nameApp folder</br>
```
from django.urls import path
from . import views

urlpatterns = [
      path('', views.nameApp, name='name'),
]
```
</br>

edit nameProject.urls to add a url for the new app</br>
```
path('', include('nameApp.urls'))
```
</br>


## Adding models

on your appName folder there is a models.py you can add models for your DB, here Item is part of a Form</br>
```
from django.db import models

class Form(models.Model0):
	name = models.CharField(max_length=40, unique=True, primary_key=True, default="name")
	description = models.CharField(max_length=512, default="description")

	def __str__(self):
		return self.name

class Item(models.Model):
	form = models.ForeignKey(Form, on_delete=models.CASCADE)

	description = models.CharField(max_length=512, default="description")
	complete = models.BooleanField(default=False)

	def __str__(self):
		return self.description
```
A item_set field will be automatically generated in the Form</br>
After that you need to migrate AND apply those migration for your DB with</br></br>
python3 manage.py makemigrations nameApp</br>
python3 manage.py migrate</br></br>
We have now a fully functionnal data base

## Fill our data base

You can do this with a lor of different ways, with the admin pannel, or with the command lines like this</br></br>
python3 manage.py shell</br>
from main.models import Item, Form</br>
form = Form(name='ShrubberyForm', description='A nice little form who generate nothing')</br>
form.save()</br>
form.item_set.create(description='Do nothing at all.')</br></br>
And that's it, if you want to verufy that your data has been added correctly just do</br></br>
Form.objects.all() OR Form.objects.get(id=1)</br>
form.item_set.all() OR form.item_set.get(id=1)</br></br>