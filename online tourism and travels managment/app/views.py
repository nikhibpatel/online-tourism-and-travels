from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate ,login as loginUser , logout 
from app.forms import BOOKINGForm
from .models import FLIGHT,BUS,TRAIN,BOOKING
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def reservation(request,**kwargs):
    if (request.method == 'GET'):
        form = BOOKINGForm()
        context = {'form':form , 'id' : kwargs['id']}
        return render(request,'booking.html',context=context)
    else:
        user=request.user
        id=kwargs['id']
        form = BOOKINGForm(request.POST)

        if form.is_valid:
            book=form
            book.user=user
            if request.session['mot']=="Flight":
                flight = FLIGHT.objects.get(pk=id)
                source = flight.source
                destination=flight.destination
                price=flight.price
                time = flight.time

            if request.session['mot']=="Train":
                train = TRAIN.objects.get(pk=id)
                source = train.source
                destination=train.destination
                price=train.price
                time = train.time

            if request.session['mot']=="Bus":
                bus = BUS.objects.get(pk=id)
                source = bus.source
                destination=bus.destination
                price=bus.price
                time = bus.time

            name = request.POST.get('name')
            age = request.POST.get('age')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            seat = request.POST.get('seat')
            total_cost = int(price) * int(seat)

            b = BOOKING(
                user=user,
                name=name,
                age=age,
                phone=phone,
                email=email,
                seat=seat,
                total_cost=total_cost,
                source=source,
                destination=destination,
                time =time,
                price=price,
                mode_of_transport=request.session['mot']
            )
            global fun
            def fun():
                return b
            
            return redirect('payment')

        else:
            context = {'form':form , 'id':id}
            return render(request,'booking.html',context=context)


@login_required(login_url='login')
def payment(request):
    if (request.method=='GET'):
        return render(request,'payment.html')
    else:
        book = fun()
        book.save()
        return redirect('print')


@login_required(login_url='login')
@login_required(login_url='reservervation')
def print_(request):
    book = fun()
    return render(request,'print.html',{'book':book})

@login_required(login_url='login')
def allBookings(request):
    user = request.user
    bookings = BOOKING.objects.filter(user=user)
    return render(request,'allBookings.html',{'bookings':bookings})

def cancelBooking(request,id):
    BOOKING.objects.get(pk=id).delete()
    return redirect('allbookings')


def buss(request):
    bus = BUS.get_all_buss()
    request.session['mot']="Bus"
    return render(request,'showBuss.html',{'buss':bus})

def flights(request):
    flight = FLIGHT.get_all_flights()
    request.session['mot']="Flight"
    return render(request,'showFlights.html',{'flights':flight})

def trains (request):
    train = TRAIN.get_all_trains()
    request.session['mot']="Train"
    return render(request,'showtrains.html',{'trains':train})

def search(request):
    mode_of_transport=request.session['mot']
    source = request.GET['source']
    destination = request.GET['destination']
    if mode_of_transport =='Bus':
        buss = BUS.objects.filter(source__icontains=source,destination__icontains=destination)
        return render(request,'showbuss.html',{'buss':buss})

    if mode_of_transport =='Flight':
        flights = FLIGHT.objects.filter(source__icontains=source,destination__icontains=destination)
        return render(request,'showflights.html',{'flights':flights})

    if mode_of_transport =='Train':
        trains = TRAIN.objects.filter(source__icontains=source,destination__icontains=destination)
        return render(request,'showtrains.html',{'trains':trains})


    

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
            return redirect('home')

        else :
            return render(request,'signup.html',context=context)


@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('home')


def index(request):
    return render(request,'index.html')

def contact(request):
    return render (request,'contact.html')

def about(request):
    return render(request,'about.html')