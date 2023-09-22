from django.urls import path
from .  import views

urlpatterns = [
    path('', views.index_page, name='index_url'),
    path('viloyat/<int:id>/',views.viloyat_page, name='viloyat_url'),
    path('vloyat/',views.viloyat_page, name='vloyat_url'),
    path('blog/',views.blog_page, name='blog_url'),
    path('contact/',views.contact_page, name='contact_url'),
    path('servise/',views.servise_page, name='servise_url'),
    path('elements/',views.elements_page, name='elemants_url')

]