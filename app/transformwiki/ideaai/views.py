from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return render(request, "ideaai/mainview.html")

def transform(request):
    return render(request, "features/transform.html")