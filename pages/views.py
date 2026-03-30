import threading

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def contact_view(request):
    if request.method == "POST":
        print("FORM SUBMITTED")

        print("USER:", settings.EMAIL_HOST_USER)

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
            Name: {name}
            Email: {email}
            
            Message:
            {message}
        """

        try:
            send_mail(subject, full_message, 'dewanisonal03@gmail.com',  ['dewanisonal03@gmail.com'], fail_silently=False)
            print("EMAIL SENT SUCCESSFULLY")
        except Exception as e:
            print("EMAIL ERROR:", e)
        return render(request, 'index.html', {'success': True, 'scroll_to': 'contact'})

    return render(request, 'index.html')