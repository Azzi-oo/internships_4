from django.shortcuts import render
from django.http import HttpResponse
import datetime


def date_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>Date and Time: {now}</body></html>"
    return HttpResponse(html)
