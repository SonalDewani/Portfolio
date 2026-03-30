from django.shortcuts import render
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


def contact_view(request):
    if request.method == "POST":
        print("FORM SUBMITTED")

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = f"New message from {name}"
        message = request.POST.get('message')

        full_message = f"""
Name: {name}
Email: {email}

Message:
{message}
"""

        try:
            message = Mail(
                from_email='dewanisonal03@gmail.com',
                to_emails='dewanisonal03@gmail.com',
                subject=subject,
                plain_text_content=full_message
            )

            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)

            print("STATUS CODE:", response.status_code)

        except Exception as e:
            print("EMAIL ERROR:", e)
            return render(request, 'index.html', {'error': str(e)})

        return render(request, 'index.html', {'success': True, 'scroll_to': 'contact'})

    return render(request, 'index.html')