from django.urls import path
from api import views

urlpatterns = [
	path('', views.homePage, name='homePage'),
    path('people/', views.homePeople, name='homePeople'),
	path('people/<int:id>', views.peopleDetails, name='peopleDetails'),
	path('form/', views.homeForm, name='homeForm'),
	path('form/<int:id>', views.formDetails, name='formDetails'),
	path('item/', views.homeItem, name='homeItem'),
	path('item/<int:id>', views.itemDetails, name='itemDetails'),
]