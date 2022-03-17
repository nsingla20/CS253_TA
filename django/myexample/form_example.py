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

# import the standard Django Forms
# from built-in library
from django import forms

# creating a form
class InputForm(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField()
	password = forms.CharField(widget = forms.PasswordInput())


from django.shortcuts import render

# Create your views here.
def form_view(request):
	context ={}
	context['form']= InputForm()
	return render(request, "home.html", context)


urlpatterns = [
    url(r'^$', form_view, name='formexample'),
]
