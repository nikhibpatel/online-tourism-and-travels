from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
#import pymysql
from firstdb.models import BOOKING
from django.template.context_processors import csrf
from django.views import generic

class BookingListView(generic.ListView):
	model = BOOKING

def getbookinginfo(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('addbookinginfo.html', c)

def addbookinginfo(request):
	pname = request.POST.get('passengername', '')
	page = request.POST.get('passengerage', '')
	pmno = request.POST.get('passenger_mno', '')
	mot = request.POST.get('mode_of_transport', '')
	adate = request.POST.get('date_of_arrival', '')
	
	if  (pmno.isnumeric() and page.isnumeric and len(pmno)==10 and len(pname)!=0 and len(page)!=0):
		s = BOOKING(passenger_name = pname, date_of_arrival=adate,passenger_age=page,passenger_mobile_no=pmno,mode_of_transport=mot)
		s.save()
		return HttpResponseRedirect('/firstdb/addsuccess/')
	else:
		return render_to_response('wrong.html')
def delbookinginfo(request):
	pname = request.POST.get('passengername', '')
	data = BOOKING.objects.filter(passenger_name = pname)
	for s in data:
		s.delete()
	return render_to_response('delrecord.html')

def addsuccess(request):
	return render_to_response('addrecord.html')
