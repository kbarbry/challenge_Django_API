from django.urls import path
from main import views

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('<int:id>', views.mainPageDetails, name='mainDetails'),
	path('createForm/',views.createForm, name='createForm'),
]
