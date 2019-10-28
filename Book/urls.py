from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.real_homepage,name='r_home'),
    path('/add_book',views.register_newbook,name='b_register'),
    path('/update_book',views.update_book,name='b_update'),
    path('/register_success',views.register_success),
    path('/description_view',views.get_description,name="desc"),
    path('/desc_view',views.get_desc),
    path('/home_page',views.real_homepage),
    path('/update_success',views.update_success),
    path('/delete_book',views.delete_book)
    ]