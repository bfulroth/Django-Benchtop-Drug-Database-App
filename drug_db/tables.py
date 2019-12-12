import django_tables2 as tables
from .models import BenchtopDrugLocations, BenchtopDrugSolubility


class DrugLocationTable(tables.Table):
    class Meta:
        model = BenchtopDrugLocations
        template_name = "django_tables2/bootstrap4.html"
        fields = ("broad_id", "barcode", "well", "plate", "conc_mM", "ori_vol_ul", "rem_vol_ul", "mw", "date_aliquoted")


class DrugSolubilityTable(tables.Table):
    class Meta:
        model = BenchtopDrugSolubility
        template_name = "django_tables2/bootstrap4.html"
        fields = ("broad_id", "buffer", "sol_um", "date", "source")