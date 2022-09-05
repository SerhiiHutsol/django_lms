from django.shortcuts import render
from django.http import HttpResponse

from .models import Groups
from .urls import qs2html

def get_groups(request):
    gr =Groups.objects.all()
    html = qs2html(gr)
    return HttpResponse(html)


