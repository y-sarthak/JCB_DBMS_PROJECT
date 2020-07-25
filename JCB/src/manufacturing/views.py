from django.shortcuts import render,get_object_or_404,redirect
from .models import Employeee,Testt,Parttt
from .forms import EmployeeForm,TestForm,partForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request,*args,**kwargs):
	context={}
	return render(request,"manufacturing/home.html",context)

# def test(request,*args,**kwargs):
# 	context={}
# 	return render(request,"manufacturing/test.html",context)
@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_employees')
def employee_form_view(request,*args,**kwargs):

	form=EmployeeForm(request.POST or None)
	
	#this is to check the validity of the form 
	if form.is_valid():
		# this is to save the form
		form.save()

		# this is to clear the values after saving
		return redirect("http://127.0.0.1:8000/list")

	my_context={
	"form":form,
	}

	return render(request,"manufacturing/employee_create.html",my_context)




@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_employees')
def employee_update(request,id,*args,**kwargs):

	obj=get_object_or_404(Employeee,id=id)
	objs=get_object_or_404(Employeee,id=id)
	form=EmployeeForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect("http://127.0.0.1:8000/list")

	elif request.method=="POST":
		objs.delete()
		return redirect("http://127.0.0.1:8000/list")

	my_context={
	"form":form,
	"object":objs
	}

	return render(request,"manufacturing/employee_update.html",my_context)



@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_employees')
def Employee_list_view(request,*args,**kwargs):
	queryset=Employeee.objects.all()
	my_context={
	"object_list":queryset,
	}

	return render(request,"manufacturing/list.html",my_context)



@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_supplies')
def test_form_view(request,*args,**kwargs):

	form=TestForm(request.POST or None)
	
	#this is to check the validity of the form 
	if form.is_valid():
		# this is to save the form
		form.save()

		# this is to clear the values after saving
		return redirect("http://127.0.0.1:8000/suplist")

	my_context={
	"form":form,
	}

	return render(request,"manufacturing/test.html",my_context)




@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_supplies')
def supplier_view(request,id,*args,**kwargs):

	obj=get_object_or_404(Testt,id=id)
	objs=get_object_or_404(Testt,id=id)
	form=TestForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect("http://127.0.0.1:8000/suplist")

	elif request.method=="POST":
		objs.delete()
		return redirect("http://127.0.0.1:8000/suplist")

	my_context={
	"form":form,
	"object":objs
	}

	return render(request,"manufacturing/supplier_view.html",my_context)




@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_supplies')
def Supplier_list_view(request,*args,**kwargs):
	queryset=Testt.objects.all()
	my_context={
	"object_list":queryset,
	}

	return render(request,"manufacturing/suplist.html",my_context)




@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_parts')
def parts_form_view(request,*args,**kwargs):

	form=partForm(request.POST or None)
	
	#this is to check the validity of the form 
	if form.is_valid():
		# this is to save the form
		form.save()

		# this is to clear the values after saving
		return redirect("http://127.0.0.1:8000/parts_list")

	my_context={
	"form":form,
	}

	return render(request,"manufacturing/part_create.html",my_context)


@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_parts')
def parts_view(request,id,*args,**kwargs):

	obj=get_object_or_404(Parttt,id=id)
	objs=get_object_or_404(Parttt,id=id)
	form=partForm(request.POST or None,instance=obj)

	if form.is_valid():
		form.save()
		return redirect("http://127.0.0.1:8000/parts_list")

	elif request.method=="POST":
		objs.delete()
		return redirect("http://127.0.0.1:8000/parts_list")

	my_context={
	"form":form,
	"object":objs
	}

	return render(request,"manufacturing/parts_view.html",my_context)


@login_required(login_url='http://127.0.0.1:8000/login_manufacturing_parts')
def Parts_list_view(request,*args,**kwargs):
	queryset=Parttt.objects.all()
	my_context={
	"object_list":queryset,
	}

	return render(request,"manufacturing/parts_list.html",my_context)