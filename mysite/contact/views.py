from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm
from .models import ContactSubmission

@require_http_methods(["GET", "POST"])
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Save submission (optional)
            ip = request.META.get('REMOTE_ADDR')
            submission = ContactSubmission.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data.get('phone', ''),
                subject=data['subject'],
                about=data['about'],
                ip_address=ip
            )

            # Prepare email content
            context = {
                'name': data['name'],
                'email': data['email'],
                'phone': data.get('phone', ''),
                'subject': data['subject'],
                'about': data['about'],
                'submission_id': submission.id,
            }
            html_content = render_to_string('contact/email_contact.html', context)
            text_content = strip_tags(html_content)

            to_email = getattr(settings, 'CONTACT_OWNER_EMAIL', settings.EMAIL_HOST_USER)
            email = EmailMultiAlternatives(
                subject=f"[New Submission] {data['subject']} — {data['name']}",
                body=text_content,
                from_email=settings.EMAIL_HOST_USER,
                to=[to_email],
                reply_to=[data['email']]  # handy for quick replies
            )
            email.attach_alternative(html_content, "text/html")
            email.send()

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})

def contact_success_view(request):
    return render(request, 'contact/success.html')
