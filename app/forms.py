from django.forms import ModelForm
from app.models import BOOKING,BUS,TRAIN,FLIGHT

class BOOKINGForm(ModelForm):
    class Meta:
        model = BOOKING
        fields = ['name','age','phone','email','seat']

class FLIGHTForm(ModelForm):
    class Meta:
        model = FLIGHT
        fields = ['source','destination','time','seat','price']


class TRAINForm(ModelForm):
    class Meta:
        model = TRAIN
        fields = ['source','destination','time','seat','price']


class BUSForm(ModelForm):
    class Meta:
        model = BUS
        fields = ['source','destination','time','seat','price']





