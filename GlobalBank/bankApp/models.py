from django.db import models

# Create your models here.
class Cust_Info(models.Model):
    account_no=models.BigIntegerField(primary_key=True,max_length=10)
    addhar=models.BigIntegerField(max_length=12)
    cust_name=models.CharField(max_length=30)
    cust_email=models.EmailField(max_length=50)
    cust_city=models.CharField(max_length=15)
    cust_dob=models.DateField(auto_now_add=True)
    cust_pass=models.CharField(max_length=10)
    img_url=models.ImageField(upload_to='images/')
    acct_st=models.CharField(max_length=7,default="False")

class Account_Info(models.Model):
    ts_id=models.BigIntegerField(primary_key=True,max_length=10)
    account_no=models.ForeignKey(Cust_Info,on_delete=models.CASCADE)
    deposit_amount=models.BigIntegerField(default=0)
    balance_amount=models.BigIntegerField(default=0)
    withdraw_amount=models.BigIntegerField(default=0)
    ts_dt = models.DateTimeField(auto_now_add=True)
    ts_st=models.CharField(max_length=6,default=False)

class Master_Account(models.Model):

    ms_id=models.BigIntegerField(primary_key=True,max_length=10)
    account_no=models.ForeignKey(Cust_Info,on_delete=models.CASCADE)
    deposit_amount=models.BigIntegerField(default=0)
    master_balance=models.BigIntegerField(default=0)
    withdraw_amount=models.BigIntegerField(default=0)
    ts_dt = models.DateTimeField(auto_now_add=True)

