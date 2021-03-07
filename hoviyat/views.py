from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage



def home(request):
	return render(request, 'hoviyat/home.html')

def signupuser(request):
	if request.method == 'GET':
		return render(request, 'hoviyat/signupuser.html', {'form':UserCreationForm()})

	else:
		#Create User
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('panel')

			except IntegrityError:
				return render(request, 'hoviyat/signupuser.html', {'form':UserCreationForm(), 'error':'Username is already taken'})

		else: #passwords don't match
			return render(request, 'hoviyat/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})


def logoutuser(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')



def panel(request):
	return render(request, 'hoviyat/panel.html')

def loginuser(request):
	if request.method == 'GET':
		return render(request, 'hoviyat/loginuser.html', {'form':AuthenticationForm()})

	else:
		user = authenticate(request, username=request.POST['username'], password=['password'])
		if user is None:
			return render(request, 'hoviyat/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
		else: 
			login(request, user)
			if request.POST['username'] == 'Ostad':
				return redirect('profpanel')
			else:	
				return redirect('panel')

def profpanel(request):
	return render(request, 'hoviyat/profpanel.html')

class home(TemplateView):
	template_name = 'home.html'


def upload(request):
	context = {}
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file)
		#url = fs.url(name)
		context['url'] = fs.url(name)
		#print(url)

	return render(request, 'hoviyat/upload.html', context)