import pytest
import requests
from json import loads

def test_id():
    r = requests.get("https://api.openbrewerydb.org/breweries?by_name=cooper")
    response = r.json()
    print(response)


    # for i in response:
    #     print (i['id'])
