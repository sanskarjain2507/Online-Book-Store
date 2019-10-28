from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("/after_admin_login",views.after_admin_login,name='admin_login_login'),
     path("/view_employees",views.view_employees),
     path("/delete_employee",views.delete_employee),
     path("/edit_employee",views.edit_employee),
     path("/updt_emp_profile",views.updt_employee),
     path("/view_profile",views.view_admin),
     path("/update_admin",views.update_admin),
     path("/on_search",views.search_work),
     path("/about_us",views.about_us),
     path("/after_login",views.on_login),
     path("/contact_us",views.contact_us),
     path("/change_password",views.change_password),
     path("/update_password",views.update_password),
     path("/access_denied",views.access_denied),
     path("/description_view",views.get_description),
     path("/view_orders",views.cust_orders),
     path("/view_feedbacks",views.cust_feedbacks),
     path("/update_adm_profile",views.update_admin_profile),


    ]