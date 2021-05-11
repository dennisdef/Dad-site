from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("gallery/", views.gallery, name="gallery"),
    path("how_we_work/", views.works, name="how_we_work"),
    path("news/", views.news, name="news"),
    path("communication/", views.communication, name="communication"),
]
