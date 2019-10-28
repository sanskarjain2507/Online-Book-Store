from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from book_store_and_library.views import encrypt,decrypt
from Book.models import Book
from my_cart.models import Cart
from Employee.models import Employee
from Customer.models import CustomerFeedback
from .models import Admin,ShopUsers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@login_required()
def after_admin_login(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        password=(decrypt(Admin.objects.filter(emailAdd=username))[0].password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user == None:
            logout(request)
            User.objects.get(username=username).delete()
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

        params = {'username': username, 'products': allprods,'role':role}
        return render(request,'Admin/after_admin_login.html',params);
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def view_employees(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username');
        employees=Employee.objects.all();
        params={'username':username,'emp':employees,'role':role}
        return render(request,'Admin/employee_information.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def delete_employee(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        id=request.POST.get('employee_id')
        emp=Employee.objects.filter(id=id)[0]
        ShopUsers.objects.filter(emailAdd=emp.emailAdd).delete()
        Employee.objects.filter(id=id).delete()
        employees = Employee.objects.all();
        User.objects.get(username=emp.emailAdd).delete()
        params = {'username': username, 'emp': employees,'role':role}
        return render(request, 'Admin/employee_information.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def edit_employee(request):
    role = request.POST.get('role')
    if role=='admin':
        username = request.POST.get('username')
        id = request.POST.get('employee_id')
        employee_info= Employee.objects.filter(id=id)
        params={'username':username,'emp':employee_info[0],'role':role}
        return render(request,'Admin/edit_employee_profile.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def updt_employee(request):
    role = request.POST.get('role')
    if role=='admin':
        admin=request.POST.get('admin')
        emp=request.POST.get('employee')
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
        salary=request.POST.get('sal')
        experience=request.POST.get('exp')

        users = ShopUsers.objects.all()
        for user in users:
            if ((user.emailAdd == email) and (user.emailAdd != emp)):
                employee_info = Employee.objects.filter(emailAdd=emp)
                params = {'username': admin, 'error': 'user already exixts','emp':employee_info[0],'role':role}
                return render(request, 'Admin/edit_employee_profile.html', params)
        password = decrypt((Employee.objects.filter(emailAdd=emp)[0]).password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user == None:
            User.objects.get(username=emp).delete()
            User.objects.create_user(username=email, password=password)
            user = authenticate(request, username=email, password=password)
            print(user)
        if user is not None:
            login(request, user)
        ShopUsers.objects.filter(emailAdd=emp).update(emailAdd=email)
        Employee.objects.filter(emailAdd=emp).update(firstName=firstname,middleName=middlename,lastName=lastname,mobileNo=mobile,empName=uname,emailAdd=email,age=age,temporaryAddress=tempAdd,tPincode=tPin,permanentAddress=permAdd,pPincode=pPin,gender=gender,salary=salary,experience=experience)
        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'username': admin, 'products': allprods,'role':role}
        return render(request, 'Admin/after_admin_login.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def view_admin(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        admin_info=Admin.objects.filter(emailAdd=username)
        params={'username':username,'adm':admin_info[0],'role':role}
        return render(request,'Admin/admin_profile.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def update_admin(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        adm_info=Admin.objects.filter(emailAdd=username)
        params = {'username': username, 'adm': adm_info[0],'role':role}
        return render(request,'Admin/update_admin.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def update_admin_profile(request):
    role = request.POST.get('role')
    if role=='admin':
        admin=request.POST.get('admin')

        firstname=request.POST.get('fname')
        middlename=request.POST.get('mname')
        lastname=request.POST.get('lname')
        mobile=request.POST.get('mobno')

        email=request.POST.get('email')
        age=request.POST.get('age')
        tempAdd=request.POST.get('tempadd')
        tPin=request.POST.get('tpin')
        permAdd=request.POST.get('permadd')
        pPin=request.POST.get('ppin')
        gender=request.POST.get('gender')
        experience=request.POST.get('exp')
        users = ShopUsers.objects.all()
        for user in users:
            if ((user.emailAdd == email) and (user.emailAdd != admin)):
                adm_info = Admin.objects.filter(emailAdd=admin)
                params = {'username': admin, 'error': 'user already exixts','adm':adm_info[0],'role':role}
                return render(request, 'Admin/update_admin.html', params)
        password = decrypt((Admin.objects.filter(emailAdd=admin)[0]).password)
        user = authenticate(request, username=email, password=password)
        print(user)
        if user == None:
            logout(request)
            User.objects.get(username=admin).delete()
            User.objects.create_user(username=email, password=password)
            user = authenticate(request, username=email, password=password)
            print(user)
        if user is not None:
            login(request, user)
        ShopUsers.objects.filter(emailAdd=admin).update(emailAdd=email)
        Admin.objects.filter(emailAdd=admin).update(firstName=firstname,middleName=middlename,lastName=lastname,mobileNo=mobile,emailAdd=email,age=age,temporaryAddress=tempAdd,tPincode=tPin,permanentAddress=permAdd,pPincode=pPin,gender=gender,experience=experience)
        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'username': email, 'products': allprods,'role':role}
        return render(request, 'Admin/after_admin_login.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def search_work(request):
    role = request.POST.get('role')
    if role=='admin':
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

            params = {'username': username, 'products': allprods,'role':role}
            return render(request,'Admin/after_admin_login.html',params)
        elif(search_by == 'category'):
            search_available=Book.objects.filter(category=search_for).exists()
            print(search_available)

            if search_available!=False:
                allprods = Book.objects.filter(category=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods,search_for],],'role':role}
                return render(request, 'Admin/after_admin_login.html', params)
            else:
                params = {'username': username, 'empty_condition':"NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Admin/after_admin_login.html', params)
        elif search_by=='book_name':
            search_available = Book.objects.filter(title=search_for).exists()
            print(search_available)

            if search_available != False:
                allprods = Book.objects.filter(title=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods,""], ],'role':role}
                return render(request, 'Admin/after_admin_login.html', params)
            else:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Admin/after_admin_login.html', params)
        elif search_by=='upl':
            src=Book.objects.filter(mrp__lte=search_for).exists()
            try:
                search_available=int(search_for)
                print(type(search_available))
            except ValueError:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Admin/after_admin_login.html', params)

            if src != False:
                allprods = Book.objects.filter(mrp__lte=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods, ""], ],'role':role}
                return render(request, 'Admin/after_admin_login.html', params)
            else:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Admin/after_admin_login.html', params)
        elif search_by=='lpl':
            src=Book.objects.filter(mrp__lte=search_for).exists()
            try:
                search_available=int(search_for)
                print(type(search_available))
            except ValueError:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Admin/after_admin_login.html', params)

            if src != False:
                allprods = Book.objects.filter(mrp__gte=search_for)
                print(allprods)
                params = {'username': username, 'products': [[allprods, ""], ],'role':role}
                return render(request, 'Admin/after_admin_login.html', params)
            else:
                params = {'username': username, 'empty_condition': "NO RESULT MATCHES YOU SEARCH",'role':role}
                return render(request, 'Admin/after_admin_login.html', params)

        else:
            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])

            params = {'username': username, 'products': allprods,'role':role}
            return render(request, 'Admin/after_admin_login.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def about_us(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        params={'username':username,'role':role}
        return render(request,'Admin/about_us.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def contact_us(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        admin_info=Admin.objects.all();
        params={'username':username,'adm':admin_info[0],'role':role}
        return render(request,'Admin/contact_us.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def change_password(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        params={'username':username,'role':role}
        return render(request,'Admin/change_admin_password.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def update_password(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        cur_pass=request.POST.get('curpass')

        adm=Admin.objects.filter(emailAdd=username)
        de_pass = decrypt(adm[0].password)
        if de_pass==cur_pass:
             new_pass=request.POST.get('newpass')
             en_newpass=encrypt(new_pass)
             Admin.objects.filter(emailAdd=username).update(password=en_newpass)
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
             return render(request, 'Admin/after_admin_login.html', params)
        else:
            params={'username':username,'pass_err':'wrong password','role':role}
            return render(request,'Admin/change_admin_password.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

def access_denied(request):
    return render(request,'Admin/access_denied.html')

@csrf_exempt
@login_required()
def on_login(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'username': username, 'products': allprods,'role':role}
        return render(request, 'Admin/after_admin_login.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def get_description(request):
    role = request.POST.get('role')
    if role=='admin':
        bid=request.POST.get('bid')
        username=request.POST.get('username')


        print(bid)
        product= Book.objects.filter(id=bid)
        params = {'username': username,'product':product[0],'role':role}
        return render(request,'Admin/book_desc.html',params)
    else:
        return render(request, 'Admin/access_denied.html')
@login_required()
def cust_orders(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        c_orders=Cart.objects.filter(status='on order').order_by('orderDate','orderId')

        params={'orders':c_orders,'username':username,'role':role}
        return render(request,'Admin/orders.html',params)
    else:
        return render(request, 'Admin/access_denied.html')
@login_required()
def cust_feedbacks(request):
    role = request.POST.get('role')
    if role=='admin':
        username=request.POST.get('username')
        fback=CustomerFeedback.objects.all().order_by('date')

        params={'fback':fback,'username':username,'role':role}
        return render(request,'Admin/feedbacks.html',params)
    else:
        return render(request, 'Admin/access_denied.html')