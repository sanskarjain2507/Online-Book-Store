"""book_store_and_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_login/',views.ad_login,name='admin_login'),
    # path("customer_login",views.cust_login,name='customer_login'),
    # path("customer_registration",views.cust_registration,name="customer_registration"),
    # path("employee_registration",views.emp_registration,name="employee_registeration")
    path('customer_login', include('Customer.urls')),
    path('employee_login', include('Employee.urls')),
    path("books",include('Book.urls')),
    path("",include('Book.urls')),
    path("admin_login",include('Admin.urls')),
    path("cart/",include('my_cart.urls')),
    path(r'media/(?P<path>.*)', serve,{'document_root': settings.MEDIA_ROOT}),
    path(r'static/(?P<path>.*)', serve,{'document_root': settings.STATIC_ROOT})

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

