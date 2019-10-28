from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.emp_login,name='employee_login'),
    path("/after_login",views.on_login),
    path('/register',views.registration,name='e_register'),
    # path('/login',views.emp_login,name='e_login'),
    path('/register_success',views.registration1),
    # path('/login_check',views.login_check),
    path('/emp_logout', views.emp_logout),
    path('/orders', views.cust_orders),
    path('/emp_profile_show', views.show_emp_profile),
    path('/on_search', views.after_search),
    path('/delivered_orders', views.delivered_orders),
    path("/about_us", views.about_us),
    path("/contact_us", views.contact_us),
    path("/change_password", views.change_password),
    path("/update_password", views.update_password),
    path("/book_description", views.get_description),
    path(r'/ajax/validate_email/', views.validate_email, name='validate_email'),
    path('/on_shipping', views.after_shipping,),
    ]