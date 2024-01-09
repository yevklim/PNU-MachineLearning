import os
import requests
import pandas as pd
from zipfile import ZipFile

cwd = os.path.abspath(os.path.dirname(__file__))

metadata_csv_path = os.path.join(cwd, 'metadata.csv')
metadata_csv = pd.read_csv(metadata_csv_path)

def code_to_url(country_code: str):
    return f'https://api.worldbank.org/v2/en/country/{country_code}?downloadformat=csv'

codes = metadata_csv['Country Code'].to_list()
urls = list(map(code_to_url, codes))

def download(url: str) -> requests.Response:
    return requests.get(url)

responses = list(map(download, urls))

dir_zipped = os.path.join(cwd, 'zipped/')
dir_extracted = os.path.join(cwd, 'extracted/')

for i in range(len(codes)):
    code = codes[i]
    response = responses[i]
    file_path = os.path.join(dir_zipped, f'{code}.zip')
    with open(file_path, mode='wb') as file:
        file.write(response.content)

for i in range(len(codes)):
    code = codes[i]
    file_path = os.path.join(dir_zipped, f'{code}.zip')
    with ZipFile(file_path) as zip:
        for file in zip.filelist:
            if file.filename.startswith('API'):
                zip.extract(file, dir_extracted)
                os.rename(os.path.join(dir_extracted, file.filename),
                          os.path.join(dir_extracted, f'{code}.csv'))
