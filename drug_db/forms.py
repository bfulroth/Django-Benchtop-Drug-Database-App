from .models import BenchtopDrugLocations
from django import forms

class FindDrugsForm(forms.ModelForm):

    class Meta:
        model = BenchtopDrugLocations
        fields = ["broad_id"]

