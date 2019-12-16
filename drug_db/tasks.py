import os
from luigi import ExternalTask, Task, LocalTarget, Parameter
from luigi.contrib.s3 import S3Target

"""
Tasks used to download the initial bench-top drug data persisted on S3 as csv files.
Note: By using parameters, the same Luigi tasks can be used to atomically download other files in the same S3 bucket.
"""

class SavedBenchDrugData(ExternalTask):
    """
    External Task which returns the aws s3 path as a target as output.
    """
    S3_BUCKET_ROOT = 's3://bfulroth-initial-bench-drugdb-data/'

    # Filename of the initial benchtop drug data saved in s3
    bench_drug_data = Parameter(default='cmpd_tbl.csv')

    def output(self):
        return S3Target(os.path.join(self.S3_BUCKET_ROOT, self.bench_drug_data))


class DownloadBenchDrugData(Task):
    """
    Luigi Task that downloads the initial data and saves the data to a csv file locally.
    """
    LOCAL_ROOT = os.path.abspath('data')

    # Filename of the initial benchtop drug data saved in s3
    bench_drug_data = Parameter(default='cmpd_tbl.csv')

    def requires(self):
        # Depends on the SavedBenchDrugData ExternalTask being complete. i.e. the file must exist on S3 in order to
        # copy it locally. By assigning the parameter of this class to the kwarg of bench_drug_data SavedBenchDrugData
        # this Task can be used to download other files specified by using the parameter.
        return SavedBenchDrugData(bench_drug_data=self.bench_drug_data)

    def output(self):
        return LocalTarget(os.path.join(self.LOCAL_ROOT, self.bench_drug_data))

    # Method that does the work of copying the files in S3 locally
    def run(self):

        with self.input().open('r') as in_f:
            result = in_f.read()

            with self.output().open('w') as out_f:
                out_f.write(result)