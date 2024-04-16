from django.urls import path
from .import views

urlpatterns=[
    path("fun/",views.fun),
    path("fun1/",views.fun1,name="fun1"),
    path("fun2/<str:f_fath>/<str:c_child>",views.fun2,name="fun2"),
    path("navbar/",views.navbar),
    path("bases/",views.bases),
    path("page1/",views.page1,name="page1"),
    path("page2/",views.page2,name="page2"),
    path("info/",views.info),

]