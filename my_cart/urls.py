from django.urls import path
from . import views

urlpatterns = [
    path("cart_orders",views.make_order),
    path("rectify_cart/<int:orderid>/<username>",views.rectified_cart),
    path("chkout_info",views.chkout_info),
    path("plc_order",views.place_order)

    ]