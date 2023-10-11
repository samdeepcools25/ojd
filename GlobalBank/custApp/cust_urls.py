from django.contrib import admin
from django.urls import path
import custApp.views  as cv
urlpatterns = [
    path('cust_board/', cv.board),
    path('deposit/<int:account>', cv.deposit),
    path('withdraw/<int:account>', cv.withdraw),
    path('checkbal/<int:account>', cv.CheckBalance),
    path('transaction/<int:account>', cv.allTransactions),

]
