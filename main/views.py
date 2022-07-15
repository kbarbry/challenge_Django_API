from tabnanny import check
from django.shortcuts import render
from .models import Form, Item, People
from .form import CreateForm

def mainPage(request):
	return render(request, 'main/home.html', {'form':'No Form Showed here'})

def mainPageDetails(request, id):
	form = Form.objects.get(id=id)

	if request.method == 'POST':
		print(request.POST)
		if request.POST.get('save'):
			for item in form.item_set.all():
				if request.POST.get('cb' + str(item.id)) == 'clicked':
					item.complete = True
				else:
					item.complete = False
				item.save()

		elif request.POST.get('newItem'):
			text = request.POST.get('newItemValue')

			if len(text) > 1:
				form.item_set.create(description=text)

	return render(request, 'main/form.html', {"form":form})

def createForm(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		
		if form.is_valid():
			n = form.cleaned_data['name']
			d = form.cleaned_data['description']
			c = form.cleaned_data['check']
			t = Form(name=n, description=d)
			t.save()

	else:
		form = CreateForm()
	return render(request, 'main/create.html', {'form':form})