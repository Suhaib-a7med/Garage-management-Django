from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path('check/', views.checkReservation, name='check'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('<int:mechanic_id>/', views.reservation, name='reservation'),
]