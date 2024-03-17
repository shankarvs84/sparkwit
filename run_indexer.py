import os

import requests
from dotenv import load_dotenv


def run_search_indexer():
    load_dotenv()
    service_name = os.environ.get('AZURE_COGNITIVE_SEARCH_SERVICE_NAME')
    azure_search_key = os.environ.get('AZURE_COGNITIVE_SEARCH_API_KEY')
    params = {'api-version': '2023-11-01'}
    headers = {'content-type': 'application/json', 'api-key': azure_search_key}
    url = f"https://{service_name}.search.windows.net/indexers/esg-automation-indexer/run"

    response = requests.post(url=url, params=params, headers=headers)

    print('response from running indexer: ', response)

    return response.status_code
