from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from main.models import Form, Item, People
from .serializers import FormSerializer, ItemSerializer, PeopleSerializer

# Home page
def homePage(request):
	return render(request, 'api/home.html', {})

# Form class
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

# Item class
@api_view(['GET', 'POST'])
def homeItem(request):
	if request.method == 'GET':
		items = Item.objects.all()
		serializer = ItemSerializer(items, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = ItemSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', "DELETE"])
def itemDetails(request, id, format=None):
	try:
		selected = Item.objects.get(pk=id)
	except Item.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = ItemSerializer(selected)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = ItemSerializer(selected, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		selected.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

# People class
@api_view(['GET', 'POST'])
def homePeople(request):
	if request.method == 'GET':
		peoples = People.objects.all()
		serializer = PeopleSerializer(peoples, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = PeopleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', "DELETE"])
def peopleDetails(request, id, format=None):
	try:
		selected = People.objects.get(pk=id)
	except People.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = PeopleSerializer(selected)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = PeopleSerializer(selected, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		selected.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)