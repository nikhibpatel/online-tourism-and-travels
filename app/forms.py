from django.forms import ModelForm
from app.models import BOOKING,BUS,TRAIN,FLIGHT

class BOOKINGForm(ModelForm):
    class Meta:
        model = BOOKING
        fields = ['name','age','phone','email','seat']




