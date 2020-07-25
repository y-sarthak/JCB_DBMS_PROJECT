from .forms import LoginForm
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def auth_login_employees(request,*args,**kwargs):
	loginform=LoginForm()
	error=None

	if request.method=='POST':
		loginform=LoginForm(request.POST)

		if loginform.is_valid():
			username=loginform.cleaned_data['username']
			password=loginform.cleaned_data['password']

			user=authenticate(username=username,password=password)

			if user:
				login(request,user)
				return HttpResponseRedirect('http://127.0.0.1:8000/list')
			else:
				error="Invalid Username or Password"


	context={
	"form":loginform,
	"error":error
	}

	return render(request,'auth/login.html',context)



def auth_login_supplies(request,*args,**kwargs):
	loginform=LoginForm()
	error=None

	if request.method=='POST':
		loginform=LoginForm(request.POST)

		if loginform.is_valid():
			username=loginform.cleaned_data['username']
			password=loginform.cleaned_data['password']

			user=authenticate(username=username,password=password)

			if user:
				login(request,user)
				return HttpResponseRedirect('http://127.0.0.1:8000/suplist')
			else:
				error="Invalid Username or Password"



	context={
	"form":loginform,
	"error":error
	}

	return render(request,'auth/login.html',context)


def auth_login_parts(request,*args,**kwargs):
	loginform=LoginForm()
	error=None

	if request.method=='POST':
		loginform=LoginForm(request.POST)

		if loginform.is_valid():
			username=loginform.cleaned_data['username']
			password=loginform.cleaned_data['password']

			user=authenticate(username=username,password=password)

			if user:
				login(request,user)
				return HttpResponseRedirect('http://127.0.0.1:8000/parts_list')
			else:
				error="Invalid Username or Password"

	context={
	"form":loginform,
	"error":error
	}

	return render(request,'auth/login.html',context)			


def logout_view(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/home")