
# Create your views here.
from django.http import HttpResponse, request, response

# Import models to be rendered as views.
from .models import BenchtopDrugLocations, BenchtopDrugSolubility

from django.views.generic import ListView, CreateView
from django_tables2 import SingleTableView
from django_tables2.export.views import ExportMixin
from .tables import DrugLocationTable, DrugSolubilityTable
from django.forms import ModelForm
from django_tables2.config import RequestConfig
from django_tables2.export.export import TableExport

from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class BenchtopDrugLocationView2(ExportMixin, SingleTableView):

    # Turn off Pagination
    SingleTableView.table_pagination = False

    model = BenchtopDrugLocations
    table_class = DrugLocationTable
    template_name = 'drug_db/basic_all_cmpd_view.html'

    #TODO: Test adding a link to download.


class BenchtopDrugSolViewAll(SingleTableView):

    # Turn off Pagination
    SingleTableView.table_pagination = False

    model = BenchtopDrugSolubility
    table_class = DrugSolubilityTable
    template_name = 'drug_db/basic_all_cmpd_view.html'


class DrugCreateView(CreateView):
    model = BenchtopDrugLocations
    fields = ("broad_id", "barcode", "well", "plate", "conc_mM",
              "ori_vol_ul", "rem_vol_ul", "mw", "date_aliquoted")

    # TODO: This shouldn't be hard coded
    success_url = '/overview/locations/'


class DrugCreateSolView(CreateView):
    model = BenchtopDrugSolubility
    fields = ("broad_id", "buffer", "sol_um", "date", "source")

    # TODO: This shouldn't be hard coded
    success_url = '/overview/solubility/'