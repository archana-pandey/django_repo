from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('home/',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('registration/',views.index, name='index'),
    path('about/',views.about, name='about'),
    # path('registration/submit/',views.studentRegistration, name='studentRegistration'),
]