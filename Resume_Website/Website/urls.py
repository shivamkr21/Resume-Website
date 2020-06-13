from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index,name='home_page'),
    url(r'^qualification$', views.qualification,name='qualification'),
    url(r'^skills$', views.skills,name='skills'),
    url(r'^experience$', views.experience,name='experience'),
    url(r'^projects$', views.projects,name='projects'),
    url(r'^achivements$', views.achivements,name='achivements'),
    url(r'^certificate$', views.certificate,name='certificate'),
    url(r'^contact$', views.contact,name='contact'),
]
