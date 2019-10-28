from django.shortcuts import render
from .form import EmployeeForm1
from .models import Employee
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from book_store_and_library.views import encrypt,decrypt
from Book.models import Book
from my_cart.models import Cart
from Admin.models import ShopUsers,Admin
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# from passlib.hash import pbkdf2_sha256

# Create your views here.

@csrf_exempt
@login_required()
def registration(request):
        role=request.POST.get('role')
        if role=='admin':
            username=request.POST.get('username')
            form = EmployeeForm1(request.POST)
            return render(request,'Employee/employee_registration.html',{'form':form,'username':username,'role':role})
        else:
            return render(request,'Admin/access_denied.html')

@csrf_exempt
@login_required()
def registration1(request):
    role=request.POST.get('role')
    if role=='admin':
        if request.method == 'POST':
            print('hello')
            form1 = EmployeeForm1(request.POST)
            # form1 = EmployeeForm(request.POST)
            if form1.is_valid():
                firstname= form1.cleaned_data['firstName']
                middlename= form1.cleaned_data['middleName']
                lastname= form1.cleaned_data['lastName']
                mobileno= form1.cleaned_data['mobileNo']
                empname= form1.cleaned_data['empName']
                password= request.POST.get('password')
                emailadd= form1.cleaned_data['emailAdd']
                salary= form1.cleaned_data['salary']
                experience= form1.cleaned_data['experience']
                age= form1.cleaned_data['age']
                tempadd= request.POST.get('temporaryAddress')
                tpincode= request.POST.get('tPincode')
                permadd= request.POST.get('permanentAddress')
                ppincode= request.POST.get('pPincode')
                gender=request.POST.get('gender')
                print('valid')

                en_password=encrypt(password)
                form = Employee()
                form.firstName = firstname
                form.middleName = middlename
                form.lastName = lastname
                form.mobileNo = mobileno
                form.empName = empname
                form.password = en_password
                form.emailAdd = emailadd
                form.salary = salary
                form.experience = experience
                form.age = age
                form.temporaryAddress = tempadd
                form.permanentAddress = permadd
                form.tPincode = tpincode
                form.pPincode =ppincode
                form.gender=gender
                form.save()
                form2 = ShopUsers()
                form2.emailAdd = emailadd
                form2.role = 'employee'
                form2.save()
                print('registerd sucess')

                user = authenticate(request, username=emailadd, password=password)
                print(user)
                if user == None:
                    User.objects.create_user(username=emailadd, password=password)
                    user = authenticate(request, username=emailadd, password=password)
                    print(user)
                if user is not None:
                    login(request, user)
                allprods = []
                catprods = Book.objects.values('category', 'id')
                cats = {item['category'] for item in catprods}
                for cat in cats:
                    prod = Book.objects.filter(category=cat)
                    allprods.append([prod, cat])
                username=request.POST.get('username')
                params = {'username': username,'role':role, 'products': allprods}
                return render(request, 'Admin/after_admin_login.html', params)
                # form.gender = request.POST.get('gender')


            else:
                print('invalid')
                print(form1.errors.as_json())
                tempadd = request.POST.get('temporaryAddress')
                tpincode = request.POST.get('tPincode')
                permadd = request.POST.get('permanentAddress')
                ppincode = request.POST.get('pPincode')
                return render(request, 'Employee/employee_registration.html', {'form': form1,'role':role,'error':'please enter correct pincode and mobile number then register again','tempadd':tempadd,'permadd':permadd,'temppin':tpincode,'permpin':ppincode})
            form=EmployeeForm1()

        return render(request, 'Employee/employee_registration.html',{'form':form,'username':username,'role':role})
    else:
        return render(request, 'Admin/access_denied.html')

def validate_email(request):
    email=request.POST.get('email',None)

    print(email)
    data = {
        'is_taken':ShopUsers.objects.filter(emailAdd=email).exists()

    }
    return JsonResponse(data)

@csrf_exempt
@login_required()
def emp_login(request):
    logout(request)
    return render(request,'Customer/login.html')


# def login_check(request):
#     username1=request.POST.get('username1')
#     password1=request.POST.get('password1')
#     users=Employee.objects.all()
#     for u in users:
#         if u.emailAdd == username1:
#
#             if decrypt(u.password)==password1:
#                 # User.objects.create_user(username=username1,password=password1)
#                 user = authenticate(request,username=username1, password=password1)
#                 print(user)
#                 if user is not  None:
#                     login(request, user)
#                 allprods = []
#                 catprods = Book.objects.values('category', 'id')
#                 cats = {item['category'] for item in catprods}
#                 for cat in cats:
#                     prod = Book.objects.filter(category=cat)
#                     allprods.append([prod, cat])
#
#                 params = {'username': username1,'products':allprods}
#                 return render(request, 'Employee/after_employee_login.html', params)
#             else:
#                 print(password1)
#                 return HttpResponse('incorrect password')
#     return HttpResponse('invalid email')

@csrf_exempt
@login_required()
def emp_logout(request):
    username=request.POST.get('username')

    logout(request)
    User.objects.get(username=username).delete()
    allprods = []
    catprods = Book.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Book.objects.filter(category=cat)
        allprods.append([prod, cat])

    params = {'products': allprods}
    return render(request, 'Book/real_homepage.html', params)

@csrf_exempt
@login_required()
def cust_orders(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        c_orders=Cart.objects.filter(status='on order').order_by('orderDate','orderId')

        params={'orders':c_orders,'username':username,'role':role,'status':'on order'}
        return render(request,'Employee/order_page.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def show_emp_profile(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        employee=Employee.objects.filter(emailAdd=username)
        params={'emp':employee[0],'username':username,'role':role}
        return render(request,'Employee/employee_profile.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def after_search(request):
    role = request.POST.get('role')
    if role=='employee':
        username = request.POST.get('username')
        search_by = request.POST.get('sel_cr')
        search_for = str(request.POST.get('srch'))
        search_for = search_for.title()
        print(type(search_for))
        print(search_for)
        print(search_by)
        if (search_by == 'selection_criteria'):
            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])

            params = {'username': username, 'products': allprods,'role':role}
            return render(request, 'Employee/after_employee_login.html', params)
        elif (search_by == 'category'):
            search_available = Book.objects.filter(category=search_for).exists()
            print(search_available)

            if search_available != False:
                allprods = Book.objects.filter(category=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods, search_for], ],'role':role}
                return render(request, 'Employee/after_employee_login.html', params)
            else:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Employee/after_employee_login.html', params)
        elif search_by == 'book_name':
            search_available = Book.objects.filter(title=search_for).exists()
            print(search_available)

            if search_available != False:
                allprods = Book.objects.filter(title=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods, ""], ],'role':role}
                return render(request, 'Employee/after_employee_login.html', params)
            else:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Employee/after_employee_login.html', params)
        elif search_by == 'upl':
            src = Book.objects.filter(mrp__lte=search_for).exists()
            try:
                search_available = int(search_for)
                print(type(search_available))
            except ValueError:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Employee/after_employee_login.html', params)

            if src != False:
                allprods = Book.objects.filter(mrp__lte=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods, ""], ],'role':role}
                return render(request, 'Employee/after_employee_login.html', params)
            else:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Employee/after_employee_login.html', params)
        elif search_by == 'lpl':
            src = Book.objects.filter(mrp__lte=search_for).exists()
            try:
                search_available = int(search_for)
                print(type(search_available))
            except ValueError:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Employee/after_employee_login.html', params)

            if src != False:
                allprods = Book.objects.filter(mrp__gte=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods, ""], ],'role':role}
                return render(request,'Employee/after_employee_login.html', params)
            else:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request,'Employee/after_employee_login.html', params)

        else:
            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])

            params = {'username': username, 'products': allprods,'role':role}
            return render(request, 'Employee/after_employee_login.html', params)

    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def after_shipping(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        order=request.POST.get('odr').split('+')[0]
        name = request.POST.get('odr').split('+')[1]
        print(order)
        Cart.objects.filter(orderId=order,orderName=name).update(status='delivered')
        c_orders=Cart.objects.filter(status='on order').order_by('orderDate','orderId')
        params = {'orders': c_orders, 'username': username,'status':'on order','role':role}
        return render(request, 'Employee/order_page.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def delivered_orders(request):
    role = request.POST.get('role')
    if role=='employee':
        username = request.POST.get('username')
        c_orders = Cart.objects.filter(status='delivered').order_by('orderDate', 'orderId')

        params = {'orders': c_orders, 'username': username,'role':role}
        return render(request, 'Employee/order_page.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def about_us(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        params={'username':username,'role':role}
        return render(request,'Employee/about_us.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def contact_us(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        admin_info=Admin.objects.all();
        params={'username':username,'adm':admin_info[0],'role':role}
        return render(request,'Employee/contact_us.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def change_password(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        params={'username':username,'role':role}
        return render(request,'Employee/change_emp_password.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def update_password(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        cur_pass=request.POST.get('curpass')

        adm=Employee.objects.filter(emailAdd=username)
        de_pass = decrypt(adm[0].password)
        if de_pass==cur_pass:
             new_pass=request.POST.get('newpass')
             en_newpass=encrypt(new_pass)
             Employee.objects.filter(emailAdd=username).update(password=en_newpass)
             user = authenticate(request, username=username, password=new_pass)
             print(user)
             if user == None:
                 User.objects.get(username=username).delete()
                 User.objects.create_user(username=username, password=new_pass)
                 user = authenticate(request, username=username, password=new_pass)
                 print(user)
             if user is not None:
                 login(request, user)
             allprods = []
             catprods = Book.objects.values('category', 'id')
             cats = {item['category'] for item in catprods}
             for cat in cats:
                 prod = Book.objects.filter(category=cat)
                 allprods.append([prod, cat])

             params = {'username': username, 'products': allprods,'role':role}
             return render(request, 'Employee/after_employee_login.html', params)
        else:
            params={'username':username,'pass_err':'wrong password','role':role}
            return render(request,'Employee/change_emp_password.html',params)
    else:
        return render(request,'Admin/access_denied.html')

@csrf_exempt
@login_required()
def get_description(request):
    role = request.POST.get('role')
    if role=='employee':
        bid=request.POST.get('bid')
        username=request.POST.get('username')


        print(bid)
        product= Book.objects.filter(id=bid)
        params = {'username': username,'product':product[0],'role':role}
        return render(request,'Employee/book_desc.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def on_login(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'username': username, 'products': allprods,'role':role}
        return render(request, 'Employee/after_employee_login.html', params)
    else:
        return render(request, 'Admin/access_denied.html')