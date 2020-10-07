from django.shortcuts import render
from django.http import HttpResponse
from workblog.models import *
from django.http import JsonResponse
from sticker import move_maschine
from pygments.formatters import HtmlFormatter

def projects(request):
    projects = Project.objects.all()
    return render(request, 'workblog/projects.html', {'projects':projects})

def project_sticker(request):
    return render(request, 'workblog/sticker.html', {})

def get_maschine_move(request, position):
    valid_position_format = [int(x) for x in str(position)]
    liszt = move_maschine('advanced', valid_position_format)
    move_data = {
        'row' : liszt[0],
        'number_of_cards' : liszt[1],
    }
    return JsonResponse(move_data)

def index(request):
    return render(request, 'workblog/index.html')

def blog(request):
    dailys = DailyKata.objects.all().order_by('-pub_date')
    return render(request, 'workblog/detail.html', {'dailys': dailys})

def resume(request):
    return render(request, 'workblog/resume.html', {})