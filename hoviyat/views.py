from django.shortcuts import render

# Create your views here.
def signupuser(request):
	return render(request, 'hoviyat/signupuser.html')