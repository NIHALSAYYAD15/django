from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<i><u><font color='Pink'>Welcome To My Webpage</u></font></i>')