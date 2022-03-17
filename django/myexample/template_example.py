from django.conf.urls import url
from django.http import HttpResponse
from django.template.loader import render_to_string

DEBUG = True
SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
ROOT_URLCONF = __name__

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/Users/nikhilsingh/TEACHING/myexample/templates/'
        ],
    },
]


def home(request):
    return HttpResponse('<h1 style="color:red">Welcome to the Demoapp\'s Homepage!</h1>')

def about(request):
    title = 'Demoapp'
    author = 'Nikhil'
    html = render_to_string('about.html', {'title': title, 'author': author})
    return HttpResponse(html)

urlpatterns = [
    url(r'^$', home, name='homepage'),
    url(r'^about/$', about, name='aboutpage'),
]
