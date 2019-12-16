from django.core.management import BaseCommand
from django.db import transaction
from ...models import BenchtopDrugLocations, BenchtopDrugSolubility


class Command(BaseCommand):
    """
    Class that can be used to purge both the drug location table as well as the solubility table. Note that the
    tables are not dropped but all records are removed. This is an atomic procedure.
    """
    help = "Model for Purging the Database by Deleting all Data in the Models."

    def handle(self, *args, **options):

        # All rows are deleted from drug_db tables. Useful for starting over.
        with transaction.atomic():
            BenchtopDrugLocations.objects.all().delete()
            BenchtopDrugSolubility.objects.all().delete()