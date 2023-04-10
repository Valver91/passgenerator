from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import GeneratorForm

from random import *
import secrets
import string

# Create your views here.
def home(request):
    generator_form = GeneratorForm()

    if request.method == "POST":
        generator_form = GeneratorForm(data=request.POST)
        if generator_form.is_valid():
            pws_lenght = int(request.POST.get('pws_lenght'))
            letters = request.POST.get('letters')
            numbers = request.POST.get('numbers')
            spec_chars = request.POST.get('spec_chars')

            if letters:
                letters = string.ascii_letters
            else:
                letters = ''
                                
            if numbers:
                numbers = string.digits
            else:
                numbers = ''
            
            if spec_chars:
                spec_chars = string.punctuation
            else:
                spec_chars = ''
                
            password = letters + numbers + spec_chars
            if not password:
                password = string.ascii_lowercase

            codigo = ''
            for i in range(pws_lenght):
                codigo += ''.join(secrets.choice(password))

            return render(request, "core/home.html", {'form':generator_form, 'codigo': codigo})
        
    return render(request, "core/home.html", {'form':generator_form})

def how_work_it(request):
    return render(request, 'core/how_work_it.html')

"""def generar(request):
    print("aqui")"""