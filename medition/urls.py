from django.conf.urls import url
from django.urls import path
from medition import views

urlpatterns = [
    url(r"^medition$", views.meditionApi),
    url(r"^medition/([0-9]+)$", views.meditionApi),
    
]
