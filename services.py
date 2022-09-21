
import os
import requests

# BETA LOCAL
api = "http:zenbus.net/provider/post.proto?apiKey=test"


def enviar_proto(valor):
    url = api
    r = requests.post(url, headers={'Content-Type': 'application/x-protobuf'}, data=valor)
    r.raise_for_status()
    return r




