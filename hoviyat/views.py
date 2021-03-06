from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



def signupuser(request):
	if request.method == 'GET':

		return render(request, 'hoviyat/signupuser.html', {'form':UserCreationForm})

	else:
		#Create User
		if request.POST['password1'] == request.POST['password2']:
			user = User.objects.create.user(request.POST['username'], password=request.POST['password1'])
			user.save()
		#else: passwords don't match