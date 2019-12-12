from django.core.management import BaseCommand
from django.db import transaction
from ...models import BenchtopDrugDB, BenchtopDrugSolubility


class Command(BaseCommand):
    help = "Model for Purging the Database by Deleting all Data in the Models."

    def handle(self, *args, **options):

        # All rows are deleted from drug_db tables. Useful for starting over.
        with transaction.atomic():
            BenchtopDrugDB.objects.all().delete()
            BenchtopDrugSolubility.objects.all().delete()