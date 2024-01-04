from django.urls import path

from adminapp import views

urlpatterns = [
    path('admin/dashboard/', views.custom_admin_dashboard, name='custom_admin_dashboard'),
    path('delete_bus/<int:bus_id>/', views.delete_bus, name='delete_bus'),
    path('edit_bus/<int:bus_id>/',views.edit_bus,name='edit_bus'),
    path('add_bus/',views.add_bus,name='add_bus'),
    path('',views.admin_home,name='admin_home'),
    path('users_list',views.user_list,name='users_list'),
    path('passenger_list',views.passenger_details,name='passenger_list'),
    path('add_stop/',views.add_stop,name='add_stop'),
    path('stop_list/',views.stop_list,name='stop_list'),
    path('delete_stop/<int:stop_id>/', views.delete_stop, name='delete_stop'),
]



