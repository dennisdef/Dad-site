import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse


def index(request):
    return render(request, "officesite/index.html")


def gallery(request):
    return render(request, "officesite/gallery.html")


def news(request):
    return render(request, "officesite/news.html")


def works(request):
    return render(request, "officesite/works.html")


def communication(request):
    return render(request, "officesite/communication.html")
