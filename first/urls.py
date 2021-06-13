from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('CustTable/', views.CustTable, name='CustTable'),
    path('<int:acc_no>/', views.Transaction, name='Trans'),
    path('formop/', views.form_input,name='form'),
    path('Transaction_history/', views.Transaction_history, name='Transaction1'),
    #path('credit/',views.form_input,name='credit')
]