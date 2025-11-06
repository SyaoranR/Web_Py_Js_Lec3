from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # (url, function, "name for reference")    
    path("alex", views.alex, name="alex"),
    path("marrie", views.marrie, name="marrie"),
    path("<str:name>", views.greet, name="greet"),
]