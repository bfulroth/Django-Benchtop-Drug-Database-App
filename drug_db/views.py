"""drub_db web page views are specified here"""
# Create your views here.
from django.http import HttpResponse

# Import models to be rendered as views.
from .models import BenchtopDrugLocations, BenchtopDrugSolubility

# Import view classes from Django and Dijango Tables 2
from django.views.generic import CreateView
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin

# Import the tables that will be converted into web page views
from .tables import DrugLocationTable, DrugSolubilityTable


class BenchtopDrugLocationView2(ExportMixin, SingleTableView):
    """Class that provides the table view for all drugs and their locations"""

    # Turn off Pagination
    SingleTableView.table_pagination = False

    model = BenchtopDrugLocations
    table_class = DrugLocationTable
    template_name = 'drug_db/basic_all_cmpd_view.html'


class BenchtopDrugSolViewAll(SingleTableView):
    """Class that provides the table view for all drug solubility results"""

    # Turn off Pagination
    SingleTableView.table_pagination = False

    model = BenchtopDrugSolubility
    table_class = DrugSolubilityTable
    template_name = 'drug_db/basic_all_cmpd_view.html'


class DrugCreateView(CreateView):
    """Class that provides the web page view of a form for entering a new drug into the location table"""
    model = BenchtopDrugLocations
    fields = ("broad_id", "barcode", "well", "plate", "conc_mM",
              "ori_vol_ul", "rem_vol_ul", "mw", "date_aliquoted")

    # On a successful insert of data, return to the url view that shows all compounds and their locations.
    success_url = '/overview/locations/'


class DrugCreateSolView(CreateView):
    """Class that provides the web page view of a form for entering the solubility info for a drug"""
    model = BenchtopDrugSolubility
    fields = ("broad_id", "buffer", "sol_um", "date", "source")

    # On a successful insert of data, return to the url view that shows all compounds and their solubility.
    success_url = '/overview/solubility/'