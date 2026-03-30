import threading

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def send_email_async(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception as e:
        print("EMAIL ERROR:", e)


def contact_view(request):
    if request.method == "POST":
        print("FORM SUBMITTED")

        print("USER:", settings.EMAIL_HOST_USER)
        print("PASS:", settings.EMAIL_HOST_PASSWORD)

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

        # 🔥 Run email in background thread
        threading.Thread(
            target=send_email_async,
            args=(subject, full_message, settings.EMAIL_HOST_USER, ['dewanisonal03@gmail.com'])
        ).start()

        return render(request, 'index.html', {'success': True, 'scroll_to': 'contact'})

    return render(request, 'index.html')