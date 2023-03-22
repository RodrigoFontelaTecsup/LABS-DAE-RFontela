from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Pagina principal")

def sumar(request,numero1,numero2):
    suma = numero1 + numero2
    return HttpResponse(f"La suma de {numero1} + {numero2} = {suma}")

def restar(request,numero1,numero2):
    resta = numero1 - numero2
    return HttpResponse(f"La resta de {numero1} - {numero2} = {resta}")

def multiplicar(request,numero1,numero2):
    multiplicacion = numero1 * numero2
    return HttpResponse(f"La multiplicacion de {numero1} * {numero2} = {multiplicacion}")