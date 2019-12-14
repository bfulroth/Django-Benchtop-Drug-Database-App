import django_tables2 as tables
from .models import BenchtopDrugLocations, BenchtopDrugSolubility


class DrugLocationTable(tables.Table):
    """Class for displaying drug location data in a web page"""

    # Add a row number
    Row = tables.TemplateColumn("{{ row_counter }}")

    class Meta:
        model = BenchtopDrugLocations
        template_name = "django_tables2/semantic.html"
        fields = ("Row", "id", "broad_id", "barcode", "well", "plate", "conc_mM",
                  "ori_vol_ul", "rem_vol_ul", "mw", "date_aliquoted")


class DrugSolubilityTable(tables.Table):
    """Class for displaying drug solubility data in a web page"""

    # Add a row number
    Row = tables.TemplateColumn("{{ row_counter }}")

    class Meta:
        model = BenchtopDrugSolubility
        template_name = "django_tables2/semantic.html"
        fields = ("Row", "id", "broad_id", "buffer", "sol_um", "date", "source")