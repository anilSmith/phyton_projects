from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
    return HttpResponse("happy uagdi")

def fun1(request):
    return render(request,"django.html")



def fun2(request,f_fath,c_child):
    fath =f_fath
    child = c_child
    
    return render (request,'django.html',{'fath':fath,'child':child})

def navbar(request):
    return render(request,"navbar.html")

def bases(request):
    return render(request,"base.html")


def info(request):
    if request.method =="POST":
        name=request.POST.get('name')
        place=request.post.get("place")
        age=request.post.get("age")
        email=request.post.get("email")
        context={"name":name,"place":place,"age":age,"email":email}
        return render(request,"info.html",context)
    return render(request,"info.html")