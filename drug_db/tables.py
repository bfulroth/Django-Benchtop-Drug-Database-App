import django_tables2 as tables
from .models import BenchtopDrugLocations

class DrugLocationTable(tables.Table):
    class Meta:
        model = BenchtopDrugLocations
        template_name = "django_tables2/bootstrap.html"
        fields = ("broad_id", "barcode", "well", "plate", "conc_mM", "ori_vol_ul", "rem_vol_ul", "mw", "date_aliquoted")