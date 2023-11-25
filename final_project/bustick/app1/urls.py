from django.contrib import admin
from django.urls import path, include
from .views import home, user_register, login_user, search_buses, signout, seat, payment_view, \
    your_backend_booking_endpoint

urlpatterns = [
    path("", home, name='home'),
    path("register/", user_register, name='register'),
    path("login/", login_user, name='login'),
    path("search/", search_buses, name='search'),
    path("signout/", signout, name='signout'),
    path("seat/", seat, name='seat'),
    path('payment/', payment_view, name='payment'),
    path('your_backend_booking_endpoint/', your_backend_booking_endpoint, name='your_backend_booking_endpoint')
]
