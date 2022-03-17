from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__


def home(request):
    return HttpResponse('<h1 style="color:red">Welcome to the Demoapp\'s Homepage!</h1>')

urlpatterns = [
    url(r'^home/$', home, name='homepage'),
]
