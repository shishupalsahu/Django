from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse(" welcome to Web pgae.! this is Home pages.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse(" welcome to Web pgae.! this is about pages.")

def contact(request):
    return HttpResponse(" welcome to Web pgae.! this is contact pages.")