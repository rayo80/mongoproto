
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

position_44 =  collection.find_one({"unidad" : 44})
print(position_44)
valor=pst.singleprotodatatest(position_44)
#valor = pst.singleprototest()
print(valor)
#sv.enviar_proto(valor)

