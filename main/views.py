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
		formAuth = CreateForm(request.POST)
		
		if formAuth.is_valid():
			forms = Form.objects.all()
			n = formAuth.cleaned_data['name']
			d = formAuth.cleaned_data['description']
			t = Form(name=n, description=d)
			t.save()
			return render(request, 'main/accessForms.html', {'forms':forms})

	else:
		formAuth = CreateForm()
	return render(request, 'main/create.html', {'form':formAuth})

def accessForms(request):
	forms = Form.objects.all()
	return render(request, 'main/accessForms.html', {'forms':forms})