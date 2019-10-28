from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import BookForm
import sys
from .models import Book
from django.contrib.auth.decorators import login_required
from my_cart.models import Cart
from .forms import BookForm
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse('wait')

@csrf_exempt
@login_required()
def register_newbook(request):
    role = request.POST.get('role')
    if role=='employee':
        form = BookForm(request.POST)
        username=request.POST.get('username')
        # user =User.objects.filter(username=username)
        # print(_user_has_perm('employee.is_employee'))
        return render(request,'Book/Book_addition.html',{'form':form,'username':username,'role':role})
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def register_success(request):
    role = request.POST.get('role')
    if role=='employee':
        username = request.POST.get('username')
        if request.method == 'POST':
            print('hello')
            form1 = BookForm(request.POST,request.FILES)
            if form1.is_valid():

                bookid = form1.cleaned_data['bookId']
                title = form1.cleaned_data['title']
                isbn = form1.cleaned_data['isbn']
                lang = form1.cleaned_data['language']
                pub = form1.cleaned_data['publisher']
                author = form1.cleaned_data['author']
                mrp = form1.cleaned_data['mrp']
                pubyear = form1.cleaned_data['publishYear']
                qty = form1.cleaned_data['quantity']
                desc = form1.cleaned_data['description']
                rating = form1.cleaned_data['rating']
                forsale=request.POST.get('sale')
                category=form1.cleaned_data['category']
                img = form1.cleaned_data['image']


                print('valid')

                form = Book()
                form.bookId = bookid
                form.title = title
                form.isbn = isbn
                form.language = lang
                form.publisher = pub
                form.author = author
                form.mrp = mrp
                form.publishYear = pubyear
                form.quantity = qty
                form.availableQuantity=qty
                form.description = desc
                form.rating = rating
                form.forSale=forsale
                form.category=category
                form.image = img
                form.save()
                print('registerd success')


            else:
                print('invalid')
                return HttpResponse('bye')
            form = BookForm()
        form=BookForm()
        return render(request, 'Book/book_addition.html', {'form': form,'username':username,'role':role})
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def update_book(request):
    role = request.POST.get('role')
    if role=='employee':
        username=request.POST.get('username')
        id=request.POST.get('bid')
        upd_item=Book.objects.filter(id=id)
        form=BookForm()
        return render(request,'Book/update_book.html',{'book':upd_item[0],'form':form,'username':username,'role':role})
    else:
        return render(request, 'Admin/access_denied.html')

def real_homepage(request):
    allprods = []
    catprods = Book.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Book.objects.filter(category=cat)
        allprods.append([prod,cat])


    params={'products':allprods}
    return render(request,'Book/real_homepage.html',params)

@csrf_exempt
@login_required()
def get_description(request):
    role = request.POST.get('role')
    if role=='customer':
        bid=request.POST.get('bid')
        username=request.POST.get('username')


        print(bid)
        product= Book.objects.filter(id=bid)
        params = {'username': username,'product':product[0],'role':role}
        return render(request,'Book/book_desc.html',params)
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def update_success(request):
    role = request.POST.get('role')
    if role=='employee':
        if request.method == 'POST':
            id=request.POST.get('bid')
            print('hello')

            bookid = request.POST.get('bookId')
            title = request.POST.get('title')
            isbn = request.POST.get('isbn')
            lang = request.POST.get('language')
            pub = request.POST.get('publisher')
            author = request.POST.get('author')
            mrp = request.POST.get('mrp')
            pubyear = request.POST.get('publishYear')
            qty = request.POST.get('quantity')
            aqty=request.POST.get('availqty')
            desc = request.POST.get('description')
            rating = request.POST.get('rating')
            forsale=request.POST.get('sale')
            category=request.POST.get('category')
            username=request.POST.get('username')
            # img = form1.cleaned_data['image']


            print('valid')

            Book.objects.filter(id=id).update(bookId=bookid,title=title,isbn=isbn,language=lang,publisher=pub,author=author,mrp=mrp,publishYear=pubyear,quantity=qty,availableQuantity=aqty,description=desc,rating=rating,forSale=forsale,category=category)

            print('registerd success')



            allprods = []
            catprods = Book.objects.values('category', 'id')
            cats = {item['category'] for item in catprods}
            for cat in cats:
                prod = Book.objects.filter(category=cat)
                allprods.append([prod, cat])

            params = {'products': allprods,'username':username,'role':role}
            return render(request, 'Employee/after_employee_login.html', params)

        else:
            print('invalid')
            return HttpResponse('bye')
    else:
        return render(request, 'Admin/access_denied.html')

@csrf_exempt
@login_required()
def delete_book(request):
    role = request.POST.get('role')
    if role=='employee':
        username = request.POST.get('username')
        id = request.POST.get('bid')
        Book.objects.filter(id=id).delete();

        allprods = []
        catprods = Book.objects.values('category', 'id')
        cats = {item['category'] for item in catprods}
        for cat in cats:
            prod = Book.objects.filter(category=cat)
            allprods.append([prod, cat])

        params = {'products': allprods, 'username': username,'role':role}
        return render(request, 'Employee/after_employee_login.html', params)
    else:
        return render(request, 'Admin/access_denied.html')

def get_desc(request):
    bid=request.POST.get('bid')
    product= Book.objects.filter(id=bid)
    params = {'product':product[0]}
    return render(request,'Book/book_desc_before_login.html',params)