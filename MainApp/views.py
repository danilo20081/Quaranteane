from django.shortcuts import render

# Create your views here.
def homeView(requests):
    context = {

    }
    return render(requests, 'MainApp/home.html', context)