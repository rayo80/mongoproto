
import os
import requests

# BETA LOCAL
parametros = {"token": "123456"}
api = "http:zenbus.net/provider/post.proto?apiKey=test"


def enviar_proto(valor):
    url = api
    r = requests.post(url, headers={'Content-Type': 'application/protobuf'}, data=valor)
    r.raise_for_status()
    return r




