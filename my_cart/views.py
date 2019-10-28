from django.shortcuts import render
from .models import Cart
from Customer.models import Customer
from Book.models import Book
import datetime
import ast
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required()
def make_order(request):
    role = request.POST.get('role')
    if role=='customer':
        username='user'
        if request.method=='POST':
            username=request.POST.get('username')
        my_prods=Cart.objects.filter(email=username)
        params={'products':my_prods,'username':username,'role':role}
        return render(request,'my_cart/cart.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def rectified_cart(request,orderid,username):
    role = request.POST.get('role')
    if role=='customer':
        Cart.objects.filter(email=username).filter(orderId=orderid).delete()
        my_prods = Cart.objects.filter(email=username)
        params = {'products': my_prods, 'username': username,'role':role}
        return render(request, 'my_cart/cart.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def chkout_info(request):
    role = request.POST.get('role')
    if role=='customer':
        username = 'user'
        if request.method == 'POST':
            username = request.POST.get('username')

        return render(request,'my_cart/after_checkout.html',{'username':username,'role':role})
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def place_order(request):
    role = request.POST.get('role')
    if role=='customer':
        cart1=request.POST.get('cart_item');
        username=request.POST.get('username')
        cust_info=Customer.objects.filter(emailAdd=username)
        print(cust_info)
        cart=ast.literal_eval(cart1)
        print(type(cart))
        currentDT=str(datetime.datetime.now())
        yyyy=currentDT[0:4]
        mo=currentDT[5:7]
        dd=currentDT[8:10]
        hh=currentDT[11:13]
        mm=currentDT[14:16]
        ss=currentDT[17:19]
        ms=currentDT[20:22]
        print(yyyy,'-',mo,'-',dd,' ',hh,':',mm,':',ss,':',ms)
        oid=dd+cust_info[0].mobileNo+mo+yyyy+ss+ms+hh+mm
        print(oid)



        for item in cart:
            print(item)
            new_order=Cart()
            new_order.orderId=oid
            new_order.orderName=cart[item][1]
            new_order.status='on order'
            new_order.email=username
            new_order.quantity=cart[item][0]
            book=Book.objects.filter(id=item)
            qty=book[0].availableQuantity
            print(qty)
            qty=qty-new_order.quantity
            Book.objects.filter(id=item).update(availableQuantity=qty)
            new_order.price=cart[item][3]
            new_order.img=cart[item][2]
            new_order.address=cust_info[0].temporaryAddress
            new_order.save();
        params={'username':username,'orderid':oid,'role':role}

        return render(request,'Customer/conform_order.html',params)
    else:
        return render(request, 'Admin/access_denied.html')
