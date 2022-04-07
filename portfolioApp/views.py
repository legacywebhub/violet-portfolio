from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import *

# Create your views here.
def home(request):
    setting = WebsiteSetting.objects.last()
    info = Info.objects.last()
    skills = Skill.objects.all()
    services = Service.objects.all()
    team = Team.objects.all()
    testimonials = Testimonial.objects.all().order_by('?')[:3]
    portfolios = Portfolio.objects.all().order_by('?')[:6]
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        try:
            email.index('@') and email.index('.')
        except ValueError:
            messages.error(request, "Please enter a valid email")
        else:
            #send_mail(f'{subject} from {name}', message, email, [info.email_1, info.email])
            message = Message(name=name, email=email, subject=subject, message=message)
            message.save()
            messages.info(request, f'Hi {name} we got your message. We will respond to you shortly.. Thanks!')


    context = {
    'teams':team,
    'skills':skills,
    'info':info,
    'services':services,
    'portfolios':portfolios,
    'setting':setting,
    'testimonials':testimonials,
    }
    return render(request, 'home.html', context)