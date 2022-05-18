from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    
    path('Game/', views.Game),
    path('ChoixJoueur/',views.ChoixJoueur),
    path('', views.index),
    


]
urlpatterns += staticfiles_urlpatterns()