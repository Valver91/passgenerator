from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            from_email = settings.EMAIL_HOST_USER

            email = EmailMessage(
                "Nuevo mensaje de contacto desde PassGenerator",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["santiagoferval@gmail.com"],
                reply_to=[from_email]
            )

            try:
                email.send()
                # Todo a ido ok, redireccionamos a OK.
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo a fallado, redireccionamos a FAIL.
                return redirect(reverse('contact')+"?fail")
            
    return render(request, 'contact/contact.html', {'form':contact_form})