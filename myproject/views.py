from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.contrib import messages

def auth_login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/company')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				messages.success(request, 'Logged in successfully')
				return HttpResponseRedirect('/company')
		else:
			print("This account has been deactivated.")
		return HttpResponse("Please enter a valid username and password")
	else:
		return render(request,'loginPage.html')

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')