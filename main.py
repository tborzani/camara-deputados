import requests
from requests import get
from collections import Counter
import time

def main():
    url = "http://suggestqueries.google.com/complete/search?client=firefox&q=Lula"
    resp = get(url).json()
    print(resp)

    url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
    resp = requests.get(url).json()
    for d in resp['dados']:
        if d['siglaUf'] == 'SP':
            print (d['nome'], d['id'], 
            d['siglaUf'], d['siglaPartido'])

if __name__ == "__main__":
    main()
