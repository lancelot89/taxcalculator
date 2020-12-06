import csv
import os
import pathlib


TAX_COLUMN_NAME = '税金種別'
TAX_COLUMN_FEE = '金額'
TAX_CSV_FILE_PATH = 'tax.csv'


class CsvModel(object):
    """Base csv model."""

    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            pathlib.Path(csv_file).touch()


class TaxModel(CsvModel):
    def __init__(self, csv_file=None, *args, **kwargs):
        if not csv_file:
            csv_file = self.get_csv_file_path()
        super().__init__(csv_file, *args, **kwargs)
        self.column = [TAX_COLUMN_NAME, TAX_COLUMN_FEE]

    def get_csv_file_path(self):
        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        if not csv_file_path:
            csv_file_path = TAX_CSV_FILE_PATH
        return csv_file_path

    def save(self, taxlist):
        with open(self.csv_file, 'w+', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            for name, fee in taxlist.items():
                writer.writerow({
                    TAX_COLUMN_NAME: name,
                    TAX_COLUMN_FEE: fee
                })
