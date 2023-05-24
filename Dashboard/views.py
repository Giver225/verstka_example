from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')


def finance(request):
    return render(request, 'dashboard/finance.html')


def team(request):
    return render(request, 'dashboard/team.html')


def contact(request):
    return render(request, 'dashboard/contact.html')


def marketplace(request):
    return render(request, 'dashboard/marketplace.html')


def profile(request):
    return render(request, 'dashboard/profile.html')
