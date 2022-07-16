from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("장고 훈련소에 오신 걸 환영합니다.")