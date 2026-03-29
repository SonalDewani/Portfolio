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
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            full_message = f"""
            Name: {name}
            Email: {email}

            Message:
            {message}
            """

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['dewanisonal03@gmail.com'],
                fail_silently=False,
            )

            return render(request, 'index.html', {'success': True, 'scroll_to': 'contact'})

        except Exception as e:
            return render(request, 'index.html', {'error': 'Something went wrong. Please try again.'})

    return render(request, 'index.html')