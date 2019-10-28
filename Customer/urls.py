from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.cust_login,name='customer_login'),
    path('/register',views.registration,name='c_register'),
    path('/login',views.cust_login,name='c_login'),
    path('/after_login',views.on_login),
    path('/register_success',views.registration1),
    path('/cust_login_success',views.login_check),
    path('/user_logout',views.user_logout),
    path('/add_to_cart', views.add_item),
    path('/cust_feedback', views.cust_feedback),
    path('/after_cust_feedback_submit', views.cust_feedback_submit),
    path('/cust_profile', views.show_cust_profile),
    path('/edit_cust_profile', views.edit_cust_profile),
    path('/updt_cust_profile', views.updt_cust_profile),
    path('/on_search', views.search_work),
    path("/about_us",views.about_us),
    path("/contact_us",views.contact_us),
    path("/after_forgot_password",views.password_retrive_info),
    path("/password_retrival_page",views.password_retrival_page),
    path("/update_password",views.update_password),
    path("/change_password", views.change_password),
    path("/updt_password", views.updt_password),
    path(r'/ajax/validate_email/', views.validate_email_cust, name='validate_email_cust')
    ]