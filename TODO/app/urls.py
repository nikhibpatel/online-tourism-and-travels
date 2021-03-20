from django.urls import path
from app.views import index,signup,login,SignOut,add_todo,delete_todo


urlpatterns = [

    path('index/', index , name="home"),
    path('signup/',signup),
    path ('login/', login , name='login'),
    path ('logout/',SignOut),
    path ('add_todo/',add_todo),
    path ('delete_todo/<int:id>',delete_todo)
]