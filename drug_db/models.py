from django.db import models
from django.db.models import DateField, ForeignKey, IntegerField, CharField, FloatField

class BenchtopDrugLocations(models.Model):
    """
    Django model class that Maps columns to Database tables for drug plate locations
    Take note that I did not link these two tables together using a foreign key. The reason is that Broad ID is not
    unique and the tube barcode is not collected during solubility testing. Unfortunately this means that the two tables
    lack referential integrity that they should have.  I'm speaking with members of my group in order to address this issue.
    """

    broad_id = CharField(verbose_name="Broad ID", max_length=22)
    barcode = IntegerField(verbose_name="Barcode", unique=True)
    well = CharField(verbose_name="Well", max_length=3)
    plate = CharField(verbose_name="Plate", max_length=8)
    conc_mM = FloatField(verbose_name= "Conc. (mM)")
    ori_vol_ul = FloatField(verbose_name="Ori. (uL)")
    rem_vol_ul = FloatField(verbose_name="Rem. (uL)")
    mw = FloatField(verbose_name="MW")
    date_aliquoted = DateField(verbose_name="Date Aliq.")

    def __str__(self):
        return "BRD: {}, BAR: {}, WELL: {}, PLATE: {}, CONC (uM): {}, Ori (uL): {}, " \
               "Rem (uL): {}, MW: {}, DATE: {}".format(self.broad_id, self.barcode, self.well, self.plate,
                                            self.conc_mM, self.ori_vol_ul, self.rem_vol_ul, self.mw, self.date_aliquoted)


class BenchtopDrugSolubility(models.Model):
    """Django model class that Maps columns to Database tables for solubility data"""

    broad_id = CharField(verbose_name="Broad ID", max_length=22)
    buffer = CharField(verbose_name="Buffer", max_length=200)
    sol_um = FloatField(verbose_name="Sol. (uM)")
    date = DateField(verbose_name='Experiment Date')
    source = CharField(verbose_name="Source", max_length=20)

    def __str__(self):
        return "BRD: {}, BUFFER: {}, SOL_UM: {}, DATE: {}, SOURCE: {}".format(self.broad_id, self.buffer, self.sol_um,
                                                                              self.date, self.source)