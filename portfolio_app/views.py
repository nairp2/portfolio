from django.shortcuts import render
from portfolio_app.models import Portfolio

# Create your views here.
def test(request):
    return render(request, "test.html", {})

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def resume(request):
    return render(request, "resume.html", {})

def portfolio_index(request):
    projects = Portfolio.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio_index.html', context)

def portfolio_detail(request, pk):
    project = Portfolio.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'portfolio_detail.html', context)

def contact(request):
    return render(request, "contact.html", {})
