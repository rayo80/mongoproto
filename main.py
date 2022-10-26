
import services as sv
import zenbus_pb2 as zpb2
from pymongo import MongoClient
import protostrings as pst

MONGO_URI= 'mongodb://localhost'
collection_name='trackers'
db_name='RomaDBgps'


client= MongoClient(MONGO_URI)
db = client[db_name]
collection=db[collection_name]

results = collection.find()

unit44 = collection.find_one({"unidad" : 44})
unit27 = collection.find({"unidad" : 27})

"""
valor=pst.singleprotodatatest(unit44)
answer = sv.enviar_proto(valor)
print(answer.json())
"""


#proveedor: tracker del padron 49
#vehiculo: detalles del vehiculo al que se asocia a la unidad 27

#single provider  pos: significa que enviaremos posiciones de un solo
#                      proveedor

valor = pst.decode_pos_forunit(unit27)
answer = sv.enviar_proto(valor)
print(answer.json())

