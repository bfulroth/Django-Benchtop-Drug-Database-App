from django.contrib import admin
from .models import BenchtopDrugLocations, BenchtopDrugSolubility

# Register both models Bench BenchtopDrugLocations and BenchtopDrugSolubility for admin access.
admin.site.register(BenchtopDrugLocations)
admin.site.register(BenchtopDrugSolubility)
