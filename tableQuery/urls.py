from django.urls import path

from . import views

app_name = 'tableQuery'

urlpatterns = [
    path(r'index/', views.index, name='index'),
    #path(r'search/', views.search, name='search'),
    path(r'fwsearch/', views.fwsearch, name='fwsearch'),
    path(r'sforms/', views.sforms, name='sforms'),
    path(r'swsc/',views.swsc,name ='swsc'),
    path(r'upload/', views.upload, name='upload'),
]