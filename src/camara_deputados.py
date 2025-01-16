import requests

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados'
resp = requests.get(url).json()
for d in resp['dados']:
    if d['siglaUf'] == 'SP':
      print (d['nome'], d['id'], 
         d['siglaUf'], d['siglaPartido'])