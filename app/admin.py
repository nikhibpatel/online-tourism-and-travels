from django.contrib import admin
from app.models import FLIGHT,BUS,TRAIN,BOOKING
# Register your models here.

admin.site.register(FLIGHT)
admin.site.register(TRAIN)
admin.site.register(BUS)
admin.site.register(BOOKING)
