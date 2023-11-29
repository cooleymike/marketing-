
from django.urls import path

from .import views

urlpatterns = [
   
    path('', views.homepage), #homepage url (.com)
    path('bookeeping/', views.bookeeping),
    path('managing/', views.managing ),
    path('confirm/', views.confirm),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload),
    path('signin/', views.signin, name="signin")


]
