from .models import BenchtopDrugLocations
from django import forms

# TODO: This class is not implemented and is in progress.
class FindDrugsForm(forms.ModelForm):

    class Meta:
        model = BenchtopDrugLocations
        fields = ["broad_id"]

