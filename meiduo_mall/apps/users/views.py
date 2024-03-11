from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from apps.users.models import User
import re

# Create your views here.
class UsernameCountView(View):

    def get(self, request, username):
        if not re.match(r'[a-zA-Z0-9_-]{5, 20}', username):
            return JsonResponse({'code': 200, 'errmsg': 'username格式错误'})
        count = User.objects.filter(username=username).count()
        return JsonResponse({'code': 0, 'count': count, 'errmsg': 'ok'})