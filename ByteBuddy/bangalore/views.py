# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def rrnagar(request):
    # message=input("Enter Hello")
    return HttpResponse("i am in RR Nagar")

def vijaynagar(request):
    # message=input("Enter Hello")
    return HttpResponse("i am in Vijay Nagar")

def punjab(request):
    message1="Hello"
    context={
        'message':message1
    }
    return render(request,'index.html',context)