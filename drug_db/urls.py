from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drug_db_basic/', views.BenchtopDrugLocationView.as_view()),
    path('drug_db_basic2/', views.BenchtopDrugLocationView2.as_view()),

]