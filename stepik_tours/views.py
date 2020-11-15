from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, данная страница не найдена((')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что-то стряслось с сервером... Скоро все починим')


class MainView(View):

    def get(self, request):
        return render(request, 'index.html')
