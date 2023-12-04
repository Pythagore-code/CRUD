from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.tache_form),
    path('list/',views.tache_list)
]