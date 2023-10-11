from django.shortcuts import render

from .models import Cust_Info,Master_Account
from django.db import transaction, DatabaseError
from django.http import HttpResponse
import random
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    return render(request,'banktemp/home.html')

#dashboard
def board(request):
     return render(request,'bankTemp/admin_board.html')

#Account open form
def openAccount(request):
       if request.method == 'POST' and request.FILES['upload']:
          na1=request.POST['na']
          adh1=request.POST['adh']
          em1=request.POST['em']
          dob1=request.POST['dob']
          pa1=request.POST['pwd']
          city=request.POST['city']
          acct_st1=False
          #
          
          account_no=random.randint(50000000,100000000)
          print(account_no)
          
          #imgdata
          upload = request.FILES['upload']
          fss = FileSystemStorage()
          file = fss.save(upload.name, upload)
          img_url1= fss.url(file)
          try:
                
              print(na1,em1,adh1,pa1,city,account_no,acct_st1)
              data=Cust_Info.objects.create(account_no=account_no,addhar=adh1,cust_name=na1,cust_email=em1,cust_city=city,cust_dob=dob1,cust_pass=pa1,img_url=img_url1,acct_st=acct_st1)
              data.save()

              #Matsrer row creation
              mst_id=random.randint(50000000,100000000)
              print(account_no)   
              master_row=Master_Account.objects.create(ms_id=mst_id,account_no_id=account_no,deposit_amount=0, master_balance=0,withdraw_amount=0)
              master_row.save()
              print("master row created for account num=",account_no)

              #email function
              subject = "Digi Bank Account Opening System"
              message = "Your account is opened successfully"+"<br>"+"your account no="+str(account_no)+"password="+str(pa1)
              sender  = "ojd4222@gmail.com"
              recipient_list=[]

              print(recipient_list.append(em1)) #Replace with the recipient's email address
              print(subject,message,sender,recipient_list)

              send_mail(subject, message, sender, recipient_list,fail_silently=False)
              print("email sent successfully")


          except DatabaseError as e:
             return HttpResponse(e)
                
          return render(request, 'bankTemp/success.html', {'file_url': img_url1})

       return render(request,'bankTemp/new_account.html')

#Dashboard Page
def newAccountRecord(request,accNo=None):
       print("accno-",accNo)
       all_accounts=Cust_Info.objects.all()
       print(all_accounts)
       acc={'account': all_accounts}

       if accNo==None:
              return render(request,'bankTemp/accounts_record.html',acc) 
             
           
                
       else:
             st=True
             data = Cust_Info.objects.get( account_no=accNo)
             data.acct_st=True
             data.save()
             print("Status has been changed")
             return render(request,'bankTemp/accounts_record.html',acc)
            
           
             
              
      # return render(request,'bankTemp/accounts_record.html',acc) 
       
def custLogin(request) :
     print("CustLogin-called")
     if request.method == 'POST':
         adh1=request.POST['adh']
         pwd=request.POST['pwd']
         print("data fro login form=",adh1,pwd)
         
         cust=Cust_Info.objects.get(addhar=adh1)
         print(cust)
        
         account_no1=cust.account_no
         print(cust.cust_pass,account_no1)

         if cust.cust_pass==pwd:
                  request.session["adh"]=cust.addhar
                  request.session["pwd"]=True
                  #return HttpResponse("Congrtas!You are logged in")
                  print("Login succesful and session stored")
                  print("session=",request.session["adh"],request.session["pwd"],request.session)
                  custProfile={'addhar':cust.addhar,'account_no': cust.account_no,'cust_name':cust.cust_name,'img':cust.img_url}
                  print(custProfile)
                  return render(request,'custTemp/cust_board.html',{'custProfile':custProfile})

         else:
                  return HttpResponse("So sad !Plz check your credentials")
                 

     return render(request,'bankTemp/login.html') 
     
    #loan
def loan(request):
      return render(request,'bankTemp/loan.html')

def contact_us(request):
      return render(request,'bankTemp/contact_us.html')
      


