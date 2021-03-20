from django.urls import path,include
from django.conf.urls import url

from firstdb import views

urlpatterns = [
   # path('', views.index, name='index'),
    url(r'^addbookinginfo/$', views.addbookinginfo),
    url(r'^delbookinginfo/$', views.delbookinginfo),
    url(r'^getbookinginfo/$', views.getbookinginfo),
    url(r'^addsuccess/$', views.addsuccess),
    path('bookings/', views.BookingListView.as_view(), name = 'bookings'),
]
