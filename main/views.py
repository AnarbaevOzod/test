from django.shortcuts import render

def read(request):
    return render(request, 'home.html')

def create(request):
    pass

def update(request,id):
    pass

def delete(request,id):
    pass