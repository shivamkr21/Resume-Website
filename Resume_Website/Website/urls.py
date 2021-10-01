from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
	url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    url(r'^$', views.index,name='home_page'),
    url(r'^qualification$', views.qualification,name='qualification'),
    url(r'^skills$', views.skills,name='skills'),
    url(r'^experience$', views.experience,name='experience'),
    url(r'^projects$', views.projects,name='projects'),
    url(r'^achivements$', views.achivements,name='achivements'),
    url(r'^certificate$', views.certificate,name='certificate'),
    url(r'^contact$', views.contact,name='contact'),
]
