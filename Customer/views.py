from django.shortcuts import render
from .models import Customer
from .form import CustomerForm
from django.http import JsonResponse
from book_store_and_library.views import encrypt,decrypt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Book.models import Book
from my_cart.models import Cart
from .models import CustomerFeedback
from Admin.models import ShopUsers
from Employee.models import Employee
from Admin.models import Admin
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def registration(request):
    print('hi')
    form = CustomerForm(request.POST)
    return render(request, 'Customer/Customer_registration.html', {'form': form})


def registration1(request):
    if request.method == 'POST':
        print('hello')
        form1 = CustomerForm(request.POST)
        # form1 = EmployeeForm(request.POST)
        if form1.is_valid():
            firstname = form1.cleaned_data['firstName']
            middlename = form1.cleaned_data['middleName']
            lastname = form1.cleaned_data['lastName']
            mobileno = form1.cleaned_data['mobileNo']
            username = form1.cleaned_data['userName']
            password1 = request.POST.get('password')
            emailadd = form1.cleaned_data['emailAdd']
            age = form1.cleaned_data['age']
            tempadd = request.POST.get('temporaryAddress')
            tpincode = request.POST.get('tPincode')
            permadd = request.POST.get('permanentAddress')
            ppincode = request.POST.get('pPincode')
            gender=request.POST.get('gender')
            print(gender)
            print('valid')
            password=encrypt(password1)
            form = Customer()
            form.firstName = firstname
            form.middleName = middlename
            form.lastName = lastname
            form.mobileNo = mobileno
            form.userName = username
            form.password = password
            form.emailAdd = emailadd
            form.age = age
            form.temporaryAddress = tempadd
            form.permanentAddress = permadd
            form.tPincode = tpincode
            form.pPincode = ppincode
            form.gender=gender
            form.save()
            form2=ShopUsers()
            form2.emailAdd=emailadd
            form2.role='customer'
            form2.save()
            print('registerd sucess')
            user = authenticate(request, username=emailadd, password=password1)
            if user==None:
                User.objects.create_user(username=emailadd,password=password1)
                user = authenticate(request, username=emailadd, password=password1)
                print(user)
            if user is not None:
                request.session['logged_user'] = emailadd
                login(request, user)
            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])
            role='customer'
            params = {'username': emailadd, 'products': allprods,'role':role}
            return render(request, 'Customer/after_login_homepage1.html', params)

        else:
            print('invalid')
            print(form1.errors)
            tempadd = request.POST.get('temporaryAddress')
            tpincode = request.POST.get('tPincode')
            permadd = request.POST.get('permanentAddress')
            ppincode = request.POST.get('pPincode')
            return render(request, 'Customer/Customer_registration.html',
                          {'form': form1, 'error': 'Please enter a valid mobile number and pincode and then register again', 'tempadd': tempadd,
                           'permadd': permadd, 'temppin': tpincode, 'permpin': ppincode})





def cust_login(request):
    logout(request)
    return render(request,'Customer/login.html',{})

@csrf_exempt
def login_check(request):
    username1=request.POST.get('username1')
    password1=request.POST.get('password1')
    isUser=ShopUsers.objects.filter(emailAdd=username1).exists()
    if isUser!= False:
        user=(ShopUsers.objects.filter(emailAdd=username1))[0].role
        if user=='customer':
            users=Customer.objects.all()
            for u in users:
                if u.emailAdd == username1:

                    if decrypt(u.password) == password1:
                        user = authenticate(request, username=username1, password=password1)
                        print(user)
                        if user==None:
                            User.objects.create_user(username=username1,password=password1)
                            user = authenticate(request, username=username1, password=password1)
                            print(user)
                        if user is not None:
                            request.session['logged_user']=username1
                            login(request, user)
                        allprods = []
                        catprods = Book.objects.values('category', 'id')
                        cats = {item['category'] for item in catprods}
                        for cat in cats:
                            prod = Book.objects.filter(category=cat)
                            allprods.append([prod, cat])
                        role='customer'
                        params={'username':username1,'role':role,'products':allprods}
                        return render(request,'Customer/after_login_homepage1.html',params)
                    else:
                        print(password1)
                        return render(request,'Customer/login.html',{'pass_error':'Incorrect Password'})
        elif user == 'employee':
            users = Employee.objects.all()
            for u in users:
                if u.emailAdd == username1:

                    if decrypt(u.password) == password1:
                        user = authenticate(request, username=username1, password=password1)
                        print(user)
                        if user==None:

                            User.objects.create_user(username=username1,password=password1)
                            user = authenticate(request, username=username1, password=password1)
                        print(user)
                        if user is not None:
                            login(request, user)
                        allprods = []
                        catprods = Book.objects.values('category', 'id')
                        cats = {item['category'] for item in catprods}
                        for cat in cats:
                            prod = Book.objects.filter(category=cat)
                            allprods.append([prod, cat])
                        role='employee'
                        params = {'username': username1,'role':role, 'products': allprods}
                        return render(request, 'Employee/after_employee_login.html', params)
                    else:
                        print(password1)
                        return render(request, 'Customer/login.html', {'pass_error': 'Incorrect Password'})
        elif user == 'admin':
            users = Admin.objects.all()
            for u in users:
                if u.emailAdd == username1:

                    if decrypt(u.password) == password1:
                        user = authenticate(request, username=username1, password=password1)
                        print(user)
                        if user==None:
                            User.objects.create_user(username=username1,password=password1)
                            user = authenticate(request, username=username1, password=password1)
                            print(user)
                        if user is not None:
                            login(request, user)
                        allprods = []
                        catprods = Book.objects.values('category', 'id')
                        cats = {item['category'] for item in catprods}
                        for cat in cats:
                            prod = Book.objects.filter(category=cat)
                            allprods.append([prod, cat])
                        role='admin'
                        params = {'username': username1,'role':role, 'products': allprods}
                        return render(request, 'Admin/after_admin_login.html', params)
                    else:
                        print(password1)
                        return render(request,'Customer/login.html',{'pass_error':'Incorrect Password'})
    else:
        return render(request,'Customer/login.html',{'email_error':'Invalid Email'})

def validate_email_cust(request):
    email=request.POST.get('email',None)

    print(email)
    data = {
        'is_taken':ShopUsers.objects.filter(emailAdd=email).exists()

    }
    return JsonResponse(data)

@login_required()
def user_logout(request):
    logout(request)
    username=""
    if request.method == 'POST':
        username=request.POST.get('username')
        print(username)
    print(username)
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
def add_item(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        bid=request.POST.get('bid')
        product=Book.objects.filter(id=bid)
        email=username
        user_prods =Cart.objects.filter(email=email)
        f=0
        for prod in user_prods:
            if prod.orderId == product[0].bookId:
                qty=prod.quantity
                qty += 1;
                order = Cart(orderId=product[0].bookId, orderName=product[0].title, email=email, quantity=qty,
                             price=product[0].mrp, img=product[0].image)
                order.save()
                f=1
                break

        if f==0:
            order = Cart(orderId=product[0].bookId, orderName=product[0].title, email=email, quantity=1,price=product[0].mrp, img=product[0].image)
            order.save()
        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'products': allprods,'username':username,'role':role}

        return render(request,'Customer/after_login_homepage1.html',params)
    else:
        return render(request, 'Admin/access_denied.html')
@csrf_exempt
@login_required()
def cust_feedback(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        params={'username':username,'role':role}
        return render(request,'Customer/customer_feedback.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def cust_feedback_submit(request):
    role = request.POST.get('role')
    if role=='customer':
        if request.method=='POST':
            username=request.POST.get('username')
            feedback=request.POST.get('feedbk')
            form = CustomerFeedback()
            form.emailAdd=username
            form.feedback=feedback
            form.save()
            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])

            params = {'username': username,'role':role, 'products': allprods}
            return render(request,'Customer/after_login_homepage1.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def show_cust_profile(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        customer=Customer.objects.filter(emailAdd=username)
        params={'cust':customer[0],'username':username,'role':role}

        return render(request,'Customer/customer_profile.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def edit_cust_profile(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        print(username)
        cust_info=Customer.objects.filter(emailAdd=username)
        print(cust_info[0])
        params={'cust':cust_info[0],'username':username,'role':role}
        return render(request,'Customer/edit_customer_profile.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def updt_cust_profile(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        firstname=request.POST.get('fname')
        middlename=request.POST.get('mname')
        lastname=request.POST.get('lname')
        mobile=request.POST.get('mobno')
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        age=request.POST.get('age')
        tempAdd=request.POST.get('tempadd')
        tPin=request.POST.get('tpin')
        permAdd=request.POST.get('permadd')
        pPin=request.POST.get('ppin')
        gender=request.POST.get('gender')
        users=ShopUsers.objects.all()
        for user in users:
            if ((user.emailAdd==email) and (user.emailAdd!=username)):
                cust_info = Customer.objects.filter(emailAdd=username)
                params={'username':username,'role':role,'error':'user already exixts','cust':cust_info[0]}
                return render(request,'Customer/edit_customer_profile.html',params)

        ShopUsers.objects.filter(emailAdd=username).update(emailAdd=email)
        Customer.objects.filter(emailAdd=username).update(firstName=firstname,middleName=middlename,lastName=lastname,mobileNo=mobile,userName=uname,emailAdd=email,age=age,temporaryAddress=tempAdd,tPincode=tPin,permanentAddress=permAdd,pPincode=pPin,gender=gender)
        password=Customer.objects.filter(emailAdd=email)[0].password
        user = authenticate(request, username=email, password=decrypt(password))
        print(user)
        if user == None:
            logout(request)
            User.objects.get(username=username).delete()
            User.objects.create_user(username=email, password=decrypt(password))
            user = authenticate(request, username=email, password=decrypt(password))
            print(user)
        if user is not None:
            login(request, user)
        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'username': email,'role':role, 'products': allprods}
        return render(request, 'Customer/after_login_homepage1.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def search_work(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        search_by=request.POST.get('sel_cr')
        search_for=str(request.POST.get('srch'))
        search_for=search_for.title()
        print(type(search_for))
        print(search_for)
        print(search_by)
        if(search_by == 'selection_criteria'):
            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])

            params = {'username': username,'role':role, 'products': allprods}
            return render(request,'Customer/after_login_homepage1.html',params)
        elif(search_by == 'category'):
            search_available=Book.objects.filter(category=search_for).exists()
            print(search_available)

            if search_available!=False:
                allprods = Book.objects.filter(category=search_for)
                print(allprods)
                params = {'username': username,'role':role, 'products': [[allprods,search_for],]}
                return render(request, 'Customer/after_login_homepage1.html', params)
            else:
                params = {'username': username,'role':role, 'empty_condition':"NO RESULT MATCHES YOU SEARCH"}
                return render(request, 'Customer/after_login_homepage1.html', params)
        elif search_by=='book_name':
            search_available = Book.objects.filter(title=search_for).exists()
            print(search_available)

            if search_available != False:
                allprods = Book.objects.filter(title=search_for)
                print(allprods)
                params = {'username': username,'role':role, 'products': [[allprods,""], ]}
                return render(request, 'Customer/after_login_homepage1.html', params)
            else:
                params = {'username': username,'role':role, 'empty_condition': "NO RESULT MATCHES YOU SEARCH"}
                return render(request, 'Customer/after_login_homepage1.html', params)
        elif search_by=='upl':
            src=Book.objects.filter(mrp__lte=search_for).exists()
            try:
                search_available=int(search_for)
                print(type(search_available))
            except ValueError:
                params = {'username': username,'role':role, 'empty_condition': "NO RESULT MATCHES YOU SEARCH"}
                return render(request, 'Customer/after_login_homepage1.html', params)

            if src != False:
                allprods = Book.objects.filter(mrp__lte=search_for)
                print(allprods)
                params = {'username': username,'role':role, 'products': [[allprods, ""], ]}
                return render(request, 'Customer/after_login_homepage1.html', params)
            else:
                params = {'username': username,'role':role, 'empty_condition': "NO RESULT MATCHES YOU SEARCH"}
                return render(request, 'Customer/after_login_homepage1.html', params)
        elif search_by=='lpl':
            src=Book.objects.filter(mrp__lte=search_for).exists()
            try:
                search_available=int(search_for)
                print(type(search_available))
            except ValueError:
                params = {'username': username,'role':role, 'empty_condition': "NO RESULT MATCHES YOU SEARCH"}
                return render(request, 'Customer/after_login_homepage1.html', params)

            if src != False:
                allprods = Book.objects.filter(mrp__gte=search_for)
                print(allprods)
                params = {'username': username,'role':role, 'products': [[allprods, ""], ]}
                return render(request, 'Customer/after_login_homepage1.html', params)
            else:
                params = {'username': username,'role':role, 'empty_condition': "NO RESULT MATCHES YOU SEARCH"}
                return render(request, 'Customer/after_login_homepage1.html', params)

        else:
            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])

            params = {'username': username,'role':role, 'products': allprods}
            return render(request, 'Customer/after_login_homepage1.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def about_us(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        params={'username':username,'role':role}
        return render(request,'Customer/about_us.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def contact_us(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        admin_info=Admin.objects.all();
        params={'username':username,'role':role,'adm':admin_info[0]}
        return render(request,'Customer/contact_us.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

def password_retrive_info(request):
    return render(request,'Customer/password_retrival_info.html')

def password_retrival_page(request):
    email=request.POST.get('username')
    username=request.POST.get('lname')

    isUser=ShopUsers.objects.filter(emailAdd=email).exists()

    if isUser!=False:

        user=(ShopUsers.objects.filter(emailAdd=email))[0].role
        params={'username':email,'role':user}
        if user=='admin':
            user_name=(Admin.objects.filter(emailAdd=email))[0].lastName

            if user_name==username:
                return render(request,'Customer/password_retrival_page.html',params)
            else:
                return render(request, 'Customer/password_retrival_info.html', {'error_data': 'Invalid Information'})

        elif user == 'employee':
            user_name = (Employee.objects.filter(emailAdd=email))[0].lastName
            if user_name == username:
                return render(request, 'Customer/password_retrival_page.html',params)
            else:
                return render(request, 'Customer/password_retrival_info.html', {'error_data': 'Invalid Information'})

        elif user=='customer':
            user_name=(Customer.objects.filter(emailAdd=email))[0].lastName
            if user_name==username:
                return render(request,'Customer/password_retrival_page.html',params)
            else:
                return render(request, 'Customer/password_retrival_info.html', {'error_data': 'Invalid Information'})

    else:
        return render(request, 'Customer/password_retrival_info.html', {'error_data': 'Invalid Information'})

def update_password(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    enpass=encrypt(password)
    role=request.POST.get('role')
    print(role)
    user = authenticate(request, username=username, password=password)
    print(user)
    if user == None:
        logout(request)
        try:
             User.objects.get(username=username).delete()
        except:
            pass
        User.objects.create_user(username=username, password=password)
        user = authenticate(request, username=username, password=password)
        print(user)
    if user is not None:
        login(request, user)
    allprods = []
    catprods = Book.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Book.objects.filter(category=cat)
        allprods.append([prod, cat])

    params = {'username': username,'role':role, 'products': allprods}
    if role=='admin':
        Admin.objects.filter(emailAdd=username).update(password=enpass)
        return render(request,'Admin/after_admin_login.html',params)
    elif role=='employee':
        Employee.objects.filter(emailAdd=username).update(password=enpass)
        return render(request, 'Employee/after_employee_login.html',params)
    elif role=='customer':
        Customer.objects.filter(emailAdd=username).update(password=enpass)
        return render(request, 'Customer/after_login_homepage1.html',params)

@csrf_exempt
@login_required()
def change_password(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        params={'username':username,'role':role}
        return render(request,'Customer/change_cust_password.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def updt_password(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        cur_pass=request.POST.get('curpass')

        adm=Customer.objects.filter(emailAdd=username)
        de_pass = decrypt(adm[0].password)
        if de_pass==cur_pass:
             new_pass=request.POST.get('newpass')
             en_newpass=encrypt(new_pass)
             Customer.objects.filter(emailAdd=username).update(password=en_newpass)
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

             params = {'username': username,'role':role, 'products': allprods}
             return render(request, 'Customer/after_login_homepage1.html', params)
        else:
            params={'username':username,'role':role,'pass_err':'wrong password'}
            return render(request, 'Customer/change_cust_password.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def on_login(request):
    role = request.POST.get('role')
    if role=='customer':
        username=request.POST.get('username')
        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'username': username, 'products': allprods,'role':role}
        return render(request, 'Customer/after_login_homepage1.html', params)
    else:
        return render(request, 'Admin/access_denied.html')