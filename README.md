# 🐍 Django 24h Challenge 🐍

## Commands to start

Dependecies:</br>
sudo apt install python3 python3-pip ipython3</br>
pip install django</br>
pip install djangorestframework</br>
pip install django-crispy-forms</br>

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
We have now a fully functionnal data base</br>

## Fill our data base

You can do this with a lor of different ways, with the admin pannel, or with the command lines like this</br></br>
python3 manage.py shell</br>
from main.models import Item, Form</br>
form = Form(name='ShrubberyForm', description='A nice little form who generate nothing')</br>
form.save()</br>
form.item_set.create(description='Do nothing at all.')</br></br>
And that's it, if you want to verufy that your data has been added correctly just do</br></br>
Form.objects.all() OR Form.objects.get(id=1)</br>
form.item_set.all() OR form.item_set.get(id=1)</br>

## Create an API

Simply create a new app called API with 2 specificity</br>
We will be using the rest_framework of django</br>
We first need to have something that convert our class in json format: a serializer</br>
```
from main.models import Form
from rest_framework import serializers

class FormSerializer(serializers.ModelSerializer):
	class Meta:
		model = Form
		fields = '__all__'
```
And we have to made one for each class, Form, Item and People.</br>
Now the second very important thing to do, is understand what http requests are</br></br>
There is 4 principal http request, GET, POST, PUT and DELETE</br></br>
GET is to get information from the data base</br>
POST is to create new data in the data base</br>
PUT is to modify/edit existing data in the data base</br>
DELETE is To delete data from the data base</br>
*things are simplified here to be comprehensive*</br></br>
An URL can be called with those request, for instance, if we call http:.../api/form/ with a GET request</br>
that probably mean you want to access data with this address, if you call the SAME url with a DELETE request</br>
that probably mean you want to delete a form.</br>
So we need to do different things on our functions depending on the request, this is waht we get:</br>
```
@api_view(['GET', 'POST'])
def homeForm(request):
	if request.method == 'GET':
		forms = Form.objects.all()
		serializer = FormSerializer(forms, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = FormSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', "DELETE"])
def formDetails(request, id, format=None):
	try:
		selected = Form.objects.get(pk=id)
	except Form.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = FormSerializer(selected)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = FormSerializer(selected, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		selected.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
```
Like we can see, we also return HTTP status to know if an operation is well made or not</br>
Some html pages are already generated to display infos of the API so we will just add a home page for </br>
the API in order to access to the different classes accessible by this one.</br>
However in order to do this, we need to learn what templates are with django</br>

## Templates with Django

With django, we can create *templates* html files.</br>
What does that mean ? Like classes on OOP, we can create objects, that can be called in html </br>
pages, to avoid code duplication, we can have variable and that kind of stuff in it to have dynamic</br>
templates we will see how good that is.</br></br>
The synthax is kinda weird but we will have a lot of {% xxx %} tags</br>
