from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bienvenidos a mi sitio de libros")