#!/usr/bin/python3
# Este modulo me permite hacer un request via http usando metodo html POST


import requests
# importamos la libreria request

url = "http://158.69.76.135/level0.php"
# definimos la url a donde queremos enviar nuestros datos

message = {'id': "1172", 'holdthedoor': 'submit'}
# definimos el payload o mensaje

# hacemos el loop de 1024 votos
for n in range(1024):
    vote = requests.post(url, data=message)
    print(vote)
