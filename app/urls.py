from django.urls import path
from app.views import index,signup,login,signout,reservation,flights,buss,trains,payment

urlpatterns = [
    path ('index/',index,name="home"),
    path('signup/',signup),
    path('login/',login , name='login'),
    path('logout/',signout),
    path('reservation/',reservation),
    path('reservation/<int:id>',reservation),
    path('flights/',flights),
    path('trains/',trains),
    path('buss/',buss),
    path('payment/',payment,name='payment')
]