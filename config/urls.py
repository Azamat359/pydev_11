from django.urls import path
from . import views
urlpatterns=[
    path('',views.homepage),
    path('detail/<int:id>/',views.detail,name='Azamat')]