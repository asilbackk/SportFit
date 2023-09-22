from django.shortcuts import render
from . import models

def index_page(request):
    sport_type = models.Sport_Type.objects.all()
    viloyat = models.Viloyat.objects.all()
    shaxar = models.Shaxar.objects.all()
    arena = models.Arena.objects.all()
    arenain = models.Arena_Index.objects.all()
    context={
        'sport_type':sport_type,
        'viloyat':viloyat,
        'shaxar':shaxar,
        'arena':arena,
        'arenain':arenain
    }
    return render(request, 'index.html',context)




def viloyat_page(request, id):
    viloyat = models.Viloyat.objects.get(id=id)

    context = {
        'viloyat':viloyat,

    }
    return render (request, 'viloyat.html', context)


def blog_page(request):
    context = {

    }
    return render(request,'blog.html',context)


def contact_page(request):
    context = {

    }
    return render (request,'contact.html',context)

def elements_page(request):
    context = {

    }
    return render(request,'elements.html',context)

def servise_page(request):
    context = {

    }
    return render (request,'services.html',context)