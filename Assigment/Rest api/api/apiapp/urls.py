from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path("", views.stdata, name="home"),
    path("getalldata/", views.getalldata, name="getalldata"),
    path("getstid/<int:id>/", views.getstid, name="getstid"),
    path("deletestid/<int:id>/", views.deletestid, name="deletestid"),
    path("savedata/", views.savedata, name="savedata"),
    path("updatedata/<int:id>/", views.updatedata, name="updatedata"),
]
