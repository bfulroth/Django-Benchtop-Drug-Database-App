from django.db import models

from django.db.models import DateField, ForeignKey, IntegerField, CharField, FloatField


class BenchtopDrugDB(models.Model):

    broad_id = CharField(max_length=22)
    barcode = IntegerField(unique=True)
    well = CharField(max_length=3)
    plate = CharField(max_length=8)
    conc_mM = FloatField()
    ori_vol_ul = FloatField()
    rem_vol_ul = FloatField()
    mw = FloatField()
    date_aliquoted = DateField()

    def __str__(self):
        return "BRD: {}, BAR: {}, WELL: {}, PLATE: {}, CONC (uM): {}, Ori (uL): {}, " \
               "Rem (uL): {}, MW: {}, DATE: {}".format(self.broad_id, self.barcode, self.well, self.plate,
                                            self.conc_mM, self.ori_vol_ul, self.rem_vol_ul, self.mw, self.date_aliquoted)


class BenchtopDrugSolubility(models.Model):

    broad_id = CharField(primary_key=22)
    buffer = CharField()
    sol_um = FloatField()
    date = DateField(verbose_name='Experiment Date')
    source = CharField()




