from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, get_object_or_404
from django.http import Http404
from home.models import Project
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.db.models import Q
import random
import re

# Create your views here.
def index(request):
    projects = Project.objects.all()
    if len(projects) < 3:
        random_projects = list(projects)
    else:
        random_projects = random.sample(list(projects), 3)
    context = {'latest_projects': random_projects}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        invalid_input = ['', ' ']
        if name in invalid_input or email in invalid_input or phone in invalid_input or message in invalid_input:
            messages.error(request, 'One or more fields are empty!')
        else:
            email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            phone_pattern = re.compile(r'^[0-9]{10}$')

            if email_pattern.match(email) and phone_pattern.match(phone):
                form_data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'message': message,
                }
                message = '''
                From:\n\t\t{}\n
                Message:\n\t\t{}\n
                Email:\n\t\t{}\n
                Phone:\n\t\t{}\n
                '''.format(form_data['name'], form_data['message'], form_data['email'], form_data['phone'])
                send_mail('You got a mail!', message, '', ['dev.ash.py@gmail.com'])
                messages.success(request, 'Your message was sent.')
                # return HttpResponseRedirect('/thanks')
            else:
                messages.error(request, 'Email or Phone is Invalid!')
    return render(request, 'contact.html', {})

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    paginator = Paginator(projects, 3)
    page = request.GET.get('page')
    projects = paginator.get_page(page)
    context = {'projects': projects}
    return render(request, 'projects.html', context)

def project(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
        context = {'project': project}
        return render(request, 'project.html', context)
    except Project.DoesNotExist:
        context = {'message': 'Project not found'}
        return render(request, '404.html', context, status=404)

def categories(request):
    all_categories = Project.objects.values('category').distinct().order_by('category')
    return render(request, "categories.html", {'all_categories': all_categories})

def category(request, category):
    category_projects = Project.objects.filter(category=category).order_by('-created_at')
    if not category_projects:
        message = f"No projects found in category: '{category}'"
        return render(request, "category.html", {"message": message})
    paginator = Paginator(category_projects, 3)
    page = request.GET.get('page')
    category_projects = paginator.get_page(page)
    return render(request, "category.html", {"category": category, 'category_projects': category_projects})

def search(request):
    query = request.GET.get('q')
    query_list = query.split()
    results = Project.objects.none()
    for word in query_list:
        results = results | Project.objects.filter(Q(title__contains=word) | Q(description__contains=word)).order_by('-created_at')
    paginator = Paginator(results, 3)
    page = request.GET.get('page')
    results = paginator.get_page(page)
    if len(results) == 0:
        message = "Sorry, no results found for your search query."
    else:
        message = ""
    return render(request, 'search.html', {'results': results, 'query': query, 'message': message})
