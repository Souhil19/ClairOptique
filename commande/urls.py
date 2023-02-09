from django.urls import path

from commande import views

urlpatterns = [
    path('checkout/', views.Commande.as_view()),
]