from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .models import *


# Create your views here.
def home(request):
    info = Info.objects.last()
    setting = WebsiteSetting.objects.last()
    skills = Skill.objects.all()
    services = Service.objects.all()
    team = Team.objects.all()
    contents = Content.objects.all()[:3]
    testimonials = Testimonial.objects.all().order_by('?')[:3]
    portfolio_categories = PortfolioCategory.objects.all()
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
            try:
                send_mail(f'{subject} from {name}', message, email, [info.email_1, info.email_2])
                message = Message(name=name, email=email, subject=subject, message=message)
                message.save()
                messages.info(request, f'Thanks {name}, we got your message and will respond to you shortly..')
            except:
                message = Message(name=name, email=email, subject=subject, message=message)
                message.save()
                messages.info(request, f'Thanks {name}, we got your message and will respond to you shortly..')

    context = {
    'teams':team,
    'skills':skills,
    'info':info,
    'contents':contents,
    'services':services,
    'portfolio_categories' :portfolio_categories,
    'portfolios':portfolios,
    'setting':setting,
    'testimonials':testimonials,
    }
    return render(request, 'home.html', context)

def portfolio(request):
    p = Paginator(Portfolio.objects.all(), 12)
    page = request.GET.get('page')
    portfolios = p.get_page(page)
    info = Info.objects.last()
    setting = WebsiteSetting.objects.last()
    context = {'portfolios':portfolios, 'setting':setting, 'info':info}
    return render(request, 'portfolio.html', context)


def contents(request):
    p = Paginator(Content.objects.all(), 12)
    page = request.GET.get('page')
    contents = p.get_page(page)
    info = Info.objects.last()
    setting = WebsiteSetting.objects.last()
    context = {'contents':contents, 'setting':setting, 'info':info}
    return render(request, 'contents.html', context)


def content(request, pk):
    content = get_object_or_404(Content, id=pk)
    info = Info.objects.last()
    setting = WebsiteSetting.objects.last()
    context = {
        'content': content,
        'setting': setting,
        'info':info,
    }
    return render(request, 'content.html', context)


def error404(request, exception):
    info = Info.objects.last()
    setting = WebsiteSetting.objects.last()
    context = {
        'setting': setting,
        'info':info,
    }
    return render(request, 'error404.html', context)


def serverError(request):
    info = Info.objects.last()
    setting = WebsiteSetting.objects.last()
    context = {
        'setting': setting,
        'info':info,
    }
    return render(request, 'serverError.html', context)