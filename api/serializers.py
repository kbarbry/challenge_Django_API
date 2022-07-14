from main.models import Form, Item, People
from rest_framework import serializers

class FormSerializer(serializers.ModelSerializer):
	class Meta:
		model = Form
		fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = '__all__'

class PeopleSerializer(serializers.ModelSerializer):
	class Meta:
		model = People
		fields = '__all__'