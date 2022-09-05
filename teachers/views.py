from django.shortcuts import render
from django.http import HttpResponse

from .models import Teachers1
from .urls import qs2html
from webargs.fields import Str, Int
from webargs.djangoparser import use_args

@use_args(
    {
        'first_name':Str(required=False),
        'experience':Int(required=False)
    },
    location="query"
)
def get_teachers(request, args):
    th = Teachers1.objects.all()
    for key, value in args.items():
        th = th.filter(**{key: value})
    html = qs2html(th)
    return HttpResponse(html)


