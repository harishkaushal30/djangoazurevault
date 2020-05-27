from django.shortcuts import render
from helloworld.azvault import AzVault

def home(request):
    secret = AzVault.getSecret('sqlusername')
    context = {
        'secret':secret,
    }
    return render(request, 'home.html', context)