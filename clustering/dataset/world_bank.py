import os
import pandas as pd

_cwd = os.path.abspath(os.path.dirname(__file__))
_src_dir = os.path.join(_cwd, 'source/world_bank/')

_xtr_dir = os.path.join(_src_dir, 'extracted/')
def get_path_to_country_csv(country_code: str) -> str:
    return os.path.join(_xtr_dir, f'{country_code}.csv')

class Metadata:
    def __init__(self) -> None:
        csv_filepath = os.path.join(_src_dir, 'metadata.csv')
        df = pd.read_csv(csv_filepath)

        self._df = df

    @property
    def data(self):
        return self._df

    @property
    def countries(self):
        return self._df['Country']

    @property
    def codes(self):
        return self._df['Country Code']

class CountyDataSet:
    def __init__(self, csv_filepath: str = None, country_code: str = None) -> None:
        if csv_filepath is None and country_code is None:
            raise Exception('Either `csv_filepath` or `country_code` must be provided.')

        if csv_filepath is None and country_code is not None:
            csv_filepath = get_path_to_country_csv(country_code)

        df = pd.read_csv(csv_filepath, header=2)
        df.drop(columns=['Country Name', 'Country Code'], inplace=True)

        indicators1: pd.DataFrame = df[['Indicator Name', 'Indicator Code']]
        indicators2: pd.DataFrame = indicators1.rename(index=df['Indicator Code'])

        df.drop(columns=['Indicator Name', 'Indicator Code'], inplace=True)

        self._df = df
        self._indicators1: pd.DataFrame = indicators1
        self._indicators2: pd.DataFrame = indicators2

    @property
    def data(self):
        return self._df

    @property
    def by_indicator_names(self) -> pd.DataFrame:
        return self._df.rename(index=self._indicators1['Indicator Name'])

    @property
    def by_indicator_codes(self) -> pd.DataFrame:
        return self._df.rename(index=self._indicators1['Indicator Code'])

    @property
    def indicators(self):
        return self._indicators1

    @property
    def indicators_names(self):
        return self._indicators1[['Indicator Name']]

    @property
    def indicators_codes(self):
        return self._indicators1[['Indicator Code']]

    @property
    def indicators_names_by_codes(self):
        return self._indicators2[['Indicator Name']]

    def indicator_name_by_code(self, code: str) -> str | None:
        return self._indicators2.T[code]['Indicator Name']
