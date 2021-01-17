from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy


def login(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def forgetPassword(request):
    return render(request, "forgetPassword.html")

def recipe(request):
    return render(request, "recipe.html")

def about(request):
    return render(request, "about.html")

def register(request):
    return render(request, "register.html")

def uploadHome(request):
    return render(request, "uploadHome.html")

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)
