from django.urls import path
from balancer_backend.views.listDrugs import views

urlpatterns = [
    path("chatgpt/list_drugs", views.medication, name="listDrugs")
] 
