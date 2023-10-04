from os import path
from . import views
from django.urls import path


urlpatterns=[
    path('rr/',views.rrnagar,name='rrnagar'),
    path('vj/',views.vijaynagar,name='vijaynagar'),
    path('pn/',views.punjab,name='punjab')
]