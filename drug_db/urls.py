from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drug_db/', views.BenchtopDrugLocationView.as_view())
]