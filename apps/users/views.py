# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View

from .models import UserProfile, FactoryInformation, OrdersDetail, ProduceTask
from .forms import LoginForm

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'login.html', {'msg': u'用户名或密码错误!'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class IndexView(View):
    def get(self, request):
        factory = FactoryInformation.objects.all()
        return render(request, 'index.html', {'factory': factory})


class DetailView(View):
    def get(self, request):
        p = request.path[11:]
        factory = FactoryInformation.objects.filter(id=int(p))
        return render(request, 'detail.html', {'factory': factory})


class OrdersView(View):
    def get(self, request):
        orders = OrdersDetail.objects.all()
        return render(request, 'ordersInfo.html', {'orders': orders})


class TaskView(View):
    def get(self, request):
        task = ProduceTask.objects.all()
        return render(request, 'task.html', {'task': task})
