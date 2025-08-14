from django.urls import path
from . import views

urlpatterns = [
    path("shorten/", views.create_short_url, name="create_short_url"),
    path("<str:code>/", views.redirect_url, name="redirect_url"),
    path("qr/<str:code>/", views.qr_code, name="qr_code"),

    
]
