from django.shortcuts import render, redirect
from core.models import Messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

def home(request):
  return render(request, 'index.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    text = request.POST.get('text')
    message = f'\nName: {name}.\nEmail: {email}.\nSubject: {subject}.\nMessage: {text}.'
    # try:
    #   validate_email('fomr777@ggjt.qux')
    # except ValidationError:
    #   alert = 'Please enter a valid email'
    #   return render(request, 'index.html', {'alert':alert})
    Messages.objects.create(
      name = name,
      email = email,
      subject = subject,
      message = text
    )
    send_mail(
      subject=subject,
      message=message,
      from_email=settings.EMAIL_HOST_USER,
      recipient_list=settings.RECIPIENT_LIST.split(','),
    )
    return redirect('home_url')