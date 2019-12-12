from django.core.management import BaseCommand
from django.db import transaction
from ...models import BenchtopDrugDB, BenchtopDrugSolubility

from luigi import build

from ...tasks import DownloadBenchDrugData


class Command(BaseCommand):
    help = "Load Initial Drug Data to SQLite DB"

    def add_arguments(self, parser):

        parser.add_argument("--purge",
                            action="store_true",
                            help="Optional flag that will purge the database before reloading.")

    def handle(self, *args, **options):

        # CLI Option to purge the DimDate and FactReview database tables before loading data.
        if options["purge"]:
            with transaction.atomic():
                BenchtopDrugDB.objects.all().delete()
                BenchtopDrugSolubility.objects.all().delete()

        # Use Luigi to Atomically download the initial data that is persisted in S3.
        build([DownloadBenchDrugData(bench_drug_data='cmpd_tbl.csv'),
               DownloadBenchDrugData(bench_drug_data='cmpd_sol_tbl.csv')], local_scheduler=True)
