from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('locations/', views.BenchtopDrugLocationView2.as_view(), name="drug_loc_overview"),
    path('solubility/', views.BenchtopDrugSolViewAll.as_view(), name="drug_sol_overview"),
    path('singleLocTbl/', views.DrugCreateView.as_view(), name="add_drug_loc_form"),
    path('singleSolTbl/', views.DrugCreateSolView.as_view(), name="add_drug_sol_form")

]