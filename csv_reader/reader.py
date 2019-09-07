import pandas as pd


class Reader:

    path_loan = ''
    path_ownership = ''

    def __init__(self, path):
        self.path_loan = path + '/loan_data.csv'
        self.path_ownership = path + '/home_ownership_data.csv'

    def get_data_set(path, skiprows, type='int32'):
        df = pd.read_csv(path, skiprows=skiprows, usecols=[0, 1])
        ds = df.values
        ds = ds.astype(type)
        return ds

    def get_loan_data(self):
        ds = Reader.get_data_set(self.path_loan, skiprows=0)
        return ds

    def get_home_ownership_data(self):
        ds = Reader.get_data_set(self.path_ownership, skiprows=0, type='str')
        return ds
