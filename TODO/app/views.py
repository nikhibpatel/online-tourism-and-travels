from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate ,login as loginUser , logout 
from django.contrib.auth.decorators import login_required
from app.forms import TODOForm
from app.models import TODO



# Create your views here.

@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
    return render(request , 'index.html' , context={'form':form,'todos':todos})

def add_todo(request):
    if request.user.is_authenticated:
        user = request.user 
        form = TODOForm(request.POST)
        if form.is_valid :
            todo = form.save(commit=False)
            todo.user=user
            todo.save()
            return redirect('home')
        else :
            return render(request , 'index.html' , context={'form':form})


def login(request):
    if(request.method == 'GET'):
        form = AuthenticationForm()
        context = {
            'form' : form 
        }
        return render(request,'login.html',context=context)
    else:
        form = AuthenticationForm(data=request.POST)
        context = {
            'form' : form 
        }


        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            loginUser(request,user)
            return redirect('home')
        else :
            return render(request,'login.html',context=context)



def signup(request):
    if (request.method == 'GET'):
        form = UserCreationForm()
        context = {
            "form" : form
        }

        return render(request,'signup.html',context=context)
    else :
        form = UserCreationForm(request.POST)
        context = {
            "form" : form
        }

        if form.is_valid() :
            form.save()
            return redirect(home)

        else :
            return render(request,'signup.html',context=context)

def delete_todo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')

def edit_todo(request,id):
    return HttpResponse("Success fullly deleted")
    



def SignOut(request):
    logout(request)
    return redirect(login)

