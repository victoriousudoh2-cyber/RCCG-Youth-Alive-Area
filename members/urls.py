from django.urls import path
from .  import views


urlpatterns=[
    path("",  views.home,  name="home"),
    path("register/",  views.register_member,  name= "register_member")
]







