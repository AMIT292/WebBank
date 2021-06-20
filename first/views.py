from first.models import Customer
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
#from .forms import updation1


def index(request):
    return render(request,"home.html")

def CustTable(request):
    customer= Customer.objects.all().order_by('acc_no')
    return render(request,"CustTable.html",{'customer': customer})
def Transaction_history(request):
    transfer=Transfer.objects.all().order_by('-id')
    return render(request,"Transaction_history.html",{'transfer':transfer })

def Transaction(request,acc_no):
    particular_cust=Customer.objects.filter(acc_no=acc_no)
    
    return render(request,"Trans.html" , {'particular_cust':particular_cust,'acc_no':acc_no} )


    
    #return (request,"CustTable.html",{'updates': updated_balance_of_reciever})
def form_input(request):
    customer= Customer.objects.all()
    # reciever details
    v1=request.POST.get('recv_acc_no')
    v2=int(request.POST.get('amt_to_transfer'))
    v3=Customer.objects.filter(acc_no=v1)
    for x in v3:
        v4=x.current_balance
        name_reciever=x.acc_holder
     # sender details
    v5=request.POST.get('sender_acc_no')
    v6=Customer.objects.filter(acc_no=v5)
    for y in v6:
        v7=y.current_balance
        name_sender=y.acc_holder

    flag=0
    #debit operation
    
    v_deb=v7-v2
    #print(v_deb)
    if (v1 != v5 and v2!=0):
        flag1=0
        if v_deb<0:
            particular_cust=Customer.objects.filter(acc_no=v5)
            flag=1
            context={'flag':flag,'particular_cust':particular_cust,'acc_no':v5}
            return render(request,"Trans.html",context)
        else:
            v_cr=v2+v4
            b=Customer.objects.filter(acc_no=v5)
            for p in b:
                p.current_balance =v_deb
                p.save()
            
            d=Customer.objects.filter(acc_no=v1)
            for q in d:
                q.current_balance =v_cr
                q.save()
            
            # transaction table entry
            sender=Customer.objects.get(acc_no=int(v5))
            tsac=Transfer.objects.create(acc_no=sender,amount_transferred=v2,acc_no_of_reciever=int(v1) , updated_balance_of_reciever=v_cr, updated_balance_of_sender=v_deb,sender_name=name_sender,reciever_name=name_reciever)
            customer= Customer.objects.all().order_by('acc_no')

            context={'flag':flag,'customer': customer}
            return render(request,"CustTable.html",context)
    else:
        flag1=1
        particular_cust=Customer.objects.filter(acc_no=v5)

        return render(request,"trans.html",{'flag1':flag1,'particular_cust':particular_cust,'acc_no':v5})
            

    #credit operation
    
    
   

    

# Create your views here.
