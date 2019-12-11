# Generated by Django 3.0 on 2019-12-11 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BenchtopDrugDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broad_id', models.CharField(max_length=22)),
                ('barcode', models.IntegerField(unique=True)),
                ('well', models.CharField(max_length=3)),
                ('plate', models.CharField(max_length=8)),
                ('conc_mM', models.FloatField()),
                ('ori_vol_ul', models.FloatField()),
                ('rem_vol_ul', models.FloatField()),
                ('mw', models.FloatField()),
                ('date_aliquoted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='BenchtopDrugSolubility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('broad_id', models.CharField(max_length=22)),
                ('buffer', models.CharField(max_length=200)),
                ('sol_um', models.FloatField()),
                ('date', models.DateField(verbose_name='Experiment Date')),
                ('source', models.CharField(max_length=20)),
            ],
        ),
    ]