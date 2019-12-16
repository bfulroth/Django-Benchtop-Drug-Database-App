from django.test import TestCase as DJTest
from .models import BenchtopDrugLocations, BenchtopDrugSolubility
from django.core.exceptions import ValidationError
from unittest import TestCase
from unittest.mock import MagicMock
from luigi.contrib.s3 import S3Target
from .tasks import SavedBenchDrugData, DownloadBenchDrugData
from luigi import LocalTarget
import os

"""Tests for drug_db App"""


class TestModels(DJTest):
    """Class for testing ORM models for app drug_db"""

    """Tests for BenchtopDrugLocations Model"""
    def test_insert_BenchtopDrugLocations_record(self):
        
        BenchtopDrugLocations.objects.create(broad_id="BRD-K00024342-001-01-9", barcode=1196291093,
                                             well="D10", plate="Plate_07", conc_mM=10, ori_vol_ul=50,
                                             rem_vol_ul=20, mw=472, date_aliquoted="2019-12-19")

    def test_insert_benchtopDrugLocations_date_wrong_formate(self):

        with self.assertRaises(ValidationError):
            BenchtopDrugLocations.objects.create(broad_id="BRD-K00024342-001-01-9", barcode=1196291093,
                                                 well="D10", plate="Plate_07", conc_mM=10, ori_vol_ul=50,
                                                 rem_vol_ul=20, mw=472, date_aliquoted="2019/12/19")

    def test_insert_benchtopDrugLocations_bar_wrong_formate(self):

        with self.assertRaises(ValueError):
            BenchtopDrugLocations.objects.create(broad_id="BRD-K00024342-001-01-9", barcode="Test",
                                                 well="D10", plate="Plate_07", conc_mM=10, ori_vol_ul=50,
                                                 rem_vol_ul=20, mw=472, date_aliquoted="2019-12-19")


    def test_get_benchtopDrugLocations_sucess(self):

        # Add record to read back
        BenchtopDrugLocations.objects.create(broad_id="BRD-K00024342-001-01-9", barcode=1196291093,
                                             well="D10", plate="Plate_07", conc_mM=10, ori_vol_ul=50,
                                             rem_vol_ul=20, mw=472, date_aliquoted="2019-12-19")

        # Check that we can pull back the BRD if it is there.
        BenchtopDrugLocations.objects.get(broad_id="BRD-K00024342-001-01-9")

    def test_get_benchtopDrugLocations_failure(self):

        # Add record to read back
        BenchtopDrugLocations.objects.create(broad_id="BRD-K00024342-001-01-9", barcode=1196291093,
                                             well="D10", plate="Plate_07", conc_mM=10, ori_vol_ul=50,
                                             rem_vol_ul=20, mw=472, date_aliquoted="2019-12-19")

        # Check that the query fails if the BRD is not there.
        with self.assertRaises(BenchtopDrugLocations.DoesNotExist):
            BenchtopDrugLocations.objects.get(broad_id="BRD-K00024343-001-01-9")


    """Tests for BenchtopDrugSolubility Model"""
    def test_insert_BenchtopDrugSolubility_record(self):
        BenchtopDrugSolubility.objects.create(broad_id="BRD-K00024342-001-01-9", buffer="This a test of buffer addition",
                                             sol_um=400, date="2019-12-19", source="Broad")

    def test_insert_BenchtopDrugSolubility_wrong_date_format(self):

        with self.assertRaises(ValidationError):
            BenchtopDrugSolubility.objects.create(broad_id="BRD-K00024342-001-01-9", buffer="This a test of buffer addition",
                                             sol_um=400, date="2019/12/19", source="Broad")

    def test_get_BenchtopDrugSolubility_success(self):

        # Add record to read back
        BenchtopDrugSolubility.objects.create(broad_id="BRD-K00024342-001-01-9", buffer="This a test of buffer addition",
                                             sol_um=400, date="2019-12-19", source="Broad")

        # Check that we can pull back the BRD if it is there.
        BenchtopDrugSolubility.objects.get(broad_id="BRD-K00024342-001-01-9")

    def test_get_BenchtopDrugSolubility_failure(self):

        # Add record to read back
        BenchtopDrugSolubility.objects.create(broad_id="BRD-K00024342-001-01-9", buffer="This a test of buffer addition",
                                             sol_um=400, date="2019-12-19", source="Broad")

        # Check that the query fails if the BRD is not there.
        with self.assertRaises(BenchtopDrugSolubility.DoesNotExist):
            BenchtopDrugSolubility.objects.get(broad_id="BRD-K00024343-001-01-9")


"""Tests for luigi tasks"""
class TestLuigiTasks(TestCase):

    def test_task_SaveBenchDrugData_class_vars(self):
        v = SavedBenchDrugData()
        self.assertEqual(v.S3_BUCKET_ROOT, 's3://bfulroth-initial-bench-drugdb-data/')

    def test_task_SaveBenchDrugData_class_param(self):
        """
        Test that the bench_drug_data Paramater defaults to 'cmpd_tbl.csv''
        """
        v = SavedBenchDrugData()
        self.assertEqual(v.bench_drug_data, 'cmpd_tbl.csv')

    def test_task_SaveBenchDrugData__output_return_S3Target(self):

        v = SavedBenchDrugData()

        result = v.output()
        self.assertEqual(result.__class__, S3Target)

    # Tests for downloading data from S3
    def test_task_DownloadBenchDrugData_class_vars(self):
        """
        Test that the luigi task has the correct class variables.
        """
        v = DownloadBenchDrugData()
        self.assertEqual(v.LOCAL_ROOT, os.path.abspath('data'))

    def test_task_DownloadBenchDrugData_class_param(self):
        """
        Test the default file to download
        """
        v = DownloadBenchDrugData()
        self.assertEqual(v.bench_drug_data, 'cmpd_tbl.csv')

    def test_task_DownloadBenchDrugData_requires(self):
        """
        Test that the requirement of the DownloadBenchDrugData task is a SavedBenchDrugData() task.
        """
        v = DownloadBenchDrugData()
        result = v.requires()
        self.assertEqual(result.__class__, SavedBenchDrugData)

    def test_task_DownloadBenchDrugData_output(self):
        """
        Test that the output of the DownloadBenchDrugData task is a LocalTarget
        """
        v = DownloadBenchDrugData()
        result = v.output()
        self.assertEqual(result.__class__, LocalTarget)

    def test_task_DownloadBenchDrugData_can_call_run(self):
        """
        Mock call the run method in the DownloadBenchDrugData task.
        :return:
        """
        real = DownloadBenchDrugData()
        real.run = MagicMock(name='run')
        real.run()
        real.run.assert_called()

