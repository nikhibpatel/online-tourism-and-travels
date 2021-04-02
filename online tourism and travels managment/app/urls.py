from django.urls import path
from app.views import index,signup,login,signout,reservation,flights,buss,trains,payment,search,contact,about,print_,allBookings,cancelBooking

urlpatterns = [
    path ('',index,name="home"),
    path('signup/',signup),
    path('login/',login , name='login'),
    path('logout/',signout),
    path('reservation/',reservation),
    path('reservation/<int:id>',reservation,name="reservation"),
    path('flights/',flights),
    path('trains/',trains),
    path('buss/',buss),
    path('search/',search),
    path('payment/',payment,name='payment'),
    path('print/',print_ , name='print'),
    path ('allBookings/',allBookings , name='allbookings'),
    path ('cancelBooking/<int:id>',cancelBooking),
    path('contact/',contact),
    path('about/',about)
]