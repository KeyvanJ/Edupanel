from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError


def signupuser(request):
	if request.method == 'GET':
		return render(request, 'hoviyat/signupuser.html', {'form':UserCreationForm})

	else:
		#Create User
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
			except IntegrityError:
				return render(request, 'hoviyat/signupuser.html', {'form':UserCreationForm(), 'error':'Username is already taken'})

		else: #passwords don't match
			return render(request, 'hoviyat/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})
