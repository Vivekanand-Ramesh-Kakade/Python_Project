from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
import secrets
import string

def generate_temp_password(length=10):
  alphabet=string.ascii_letters + string.digits
  return ''.join(secrets.choice(alphabet) for _ in range(length)) 

def create_user_and_send_temp_password(request):
    # Example: hardcoded user info (replace with form input or API)
    username = "newuser"
    email = "newuser@example.com"

    # Generate random password
    temp_password = generate_temp_password()

    # Create user
    user = User.objects.create_user(
        username=username,
        email=email,
        password=temp_password
    )
    user.is_active = True
    user.save()

    # Prepare email
    subject = "Welcome! Your temporary password"
    message = (
        f"Hello {username},\n\n"
        f"Your account has been created. Use the following temporary password to log in:\n\n"
        f"{temp_password}\n\n"
        "For security, please change your password after logging in.\n\n"
        "Best regards,\nApplication Team"
    )

    # Send email
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

    return HttpResponse(f"User {username} created and email sent to {email}.")
