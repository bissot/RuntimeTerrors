from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'calendarModule/homepage.html')

def login(request):
    return render(request, 'calendarModule/login.html')
    
def meetings(request):
    return render(request, 'calendarModule/meetings.html')
    
def form(request):
    return render(request, 'calendarModule/form.html')