from django.contrib import admin
from django.urls import path
import bankApp.views  as bv
urlpatterns = [
 
    path('bank_board/', bv.board),
    path('new-account/', bv.openAccount),
    path('acc_record/',bv.newAccountRecord),
    path('acc_record/<int:accNo>/',bv.newAccountRecord),
    path('login/',bv.custLogin),
    path('loan/',bv.loan),
    path('contact_us/',bv.contact_us),
]
