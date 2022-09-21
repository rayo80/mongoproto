
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
print(unit27)
valor=pst.singleprotodatatest(unit44)

#valor = pst.double_prototest()
valor = pst.decode_pos_forunit(unit27)
#sv.enviar_proto(valor)

