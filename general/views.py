from django.shortcuts import render
from django.http import HttpResponse
import datetime
# from general.models import User
# from general.managers import CustomUserManager


def date_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>Date and Time: {now}</body></html>"
    return HttpResponse(html)


# def my_view(request):
#     users_with_many_friends = User.objects.users_with_many_friends()
#     for user in users_with_many_friends:
#         print(user.username)

