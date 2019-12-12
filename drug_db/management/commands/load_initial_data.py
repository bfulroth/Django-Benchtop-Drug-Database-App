import os
from django.core.management import BaseCommand
from django.db import transaction
from ...models import BenchtopDrugLocations, BenchtopDrugSolubility

from luigi import build
from ...tasks import DownloadBenchDrugData
import pandas as pd


class Command(BaseCommand):
    """Class that extents BaseCommand that provides the ability to download the initial drug data from S3."""
    help = "Load Initial Drug Data to SQLite DB"

    def add_arguments(self, parser):

        parser.add_argument("--purge",
                            action="store_true",
                            help="Optional flag that will purge the database before reloading.")

    def handle(self, *args, **options):

        # CLI Option to purge the DimDate and FactReview database tables before loading data.
        if options["purge"]:
            with transaction.atomic():
                BenchtopDrugLocations.objects.all().delete()
                BenchtopDrugSolubility.objects.all().delete()

        # Path where data should be stored.
        ROOT = os.path.abspath('data')

        # Files to download
        cmpd_tbl = 'cmpd_tbl.csv'
        cmpd_sol_tbl = 'cmpd_sol_tbl.csv'

        # Use Luigi to Atomically download the initial data that is persisted in S3.
        build([DownloadBenchDrugData(bench_drug_data=cmpd_tbl),
               DownloadBenchDrugData(bench_drug_data=cmpd_sol_tbl)], local_scheduler=True)


        # As rows will likely never be greater than 1000 a decision was made to use Pandas in memory DataFrames vs. Dask
        # Get the absolute path.

        df_drug_data = pd.read_csv(os.path.join(ROOT, cmpd_tbl))
        df_drug_sol_data = pd.read_csv(os.path.join(ROOT, cmpd_sol_tbl))

        #Atomically load the data to SQLlite DB
        # Load drug location data.
        with transaction.atomic():
            for idx, row in df_drug_data.iterrows():
                BenchtopDrugLocations.objects.create(broad_id=row['Broad_ID'],
                                                     barcode=row['Barcode'],
                                                     well=row['Well'],
                                                     plate=row['Plate'],
                                                     conc_mM=row['Conc_mM'],
                                                     ori_vol_ul=row['Ori_Vol_uL'],
                                                     rem_vol_ul=row['Rem_Vol_uL'],
                                                     mw=row['MW'],
                                                     date_aliquoted=row['Date_Aliquoted'])

        # Load drug solubility data.
        with transaction.atomic():
            for idx, row in df_drug_sol_data.iterrows():
                BenchtopDrugSolubility.objects.create(broad_id=row['Broad_ID'],
                                                      buffer=row['Buffer'],
                                                      sol_um=row['Sol_uM'],
                                                      date=row['Exp_Date'],
                                                      source=row['Source'])


        print("Data loading complete!")
