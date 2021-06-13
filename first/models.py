from django.db import models
from django.db.models import Model
from django.utils import timezone


class Customer(models.Model):
    acc_no= models.IntegerField(primary_key=True)
    acc_holder = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=254)
    current_balance = models.IntegerField(default=0)

    def __str__(self):
        return str(self.acc_no)


class Transfer(models.Model):
    acc_no=models.ForeignKey(Customer,on_delete=models.CASCADE)
    amount_transferred = models.IntegerField(default=0)
    acc_no_of_reciever = models.IntegerField(default=0)
    updated_balance_of_reciever= models.IntegerField(default=0)
    updated_balance_of_sender= models.IntegerField(default=0)
    sender_name=models.CharField(max_length=100)
    reciever_name=models.CharField(max_length=100)
    Date_and_time=models.DateTimeField(default=timezone.now )

    """def __str__(self):
        
        return self.acc_no"""
# Create your models here.
