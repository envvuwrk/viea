from django.urls import path
from . import views

app_name = 'awardapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('calendar/',views.calendar,name='calendar'),
    path('gallery/',views.gallery,name='gallery'),
    # path('register/',views.register,name='register'),

]
