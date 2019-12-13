from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drug_db_basic/', views.BenchtopDrugLocationView.as_view()),
    path('locations/', views.BenchtopDrugLocationView2.as_view(), name="drug_loc_overview"),
    path('solubility/', views.BenchtopDrugSolViewAll.as_view(), name="drug_sol_overview"),
    path('form/', views.DrugCreateView.as_view())

]