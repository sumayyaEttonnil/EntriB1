from django.urls import path,include
from . import views
urlpatterns = [

    path("", views.home,name="homepage"),
    path("kids/",views.kids,name="kidspage"),
    path("register/",views.register,name="register"),
    path("login/",views.logine,name="login"),
    path("logout/",views.logout_user,name="logout"),
]