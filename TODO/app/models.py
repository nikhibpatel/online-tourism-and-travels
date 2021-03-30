from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TODO(models.Model):
    status_choices = [
        ('c','complete'),
        ('p','pending')
    ]

    priority_choices = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    ]

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=30,choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    priority =  models.CharField(max_length=2,choices=priority_choices)
