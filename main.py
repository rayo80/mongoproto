
import services as sv
import zenbus_pb2 as zpb2
import protostrings as pst
from pymongo import MongoClient


MONGO_URI= 'mongodb://localhost'
collection_name='trackers'
db_name='RomaDBgps'


client= MongoClient(MONGO_URI)
db = client[db_name]
collection=db[collection_name]

results = collection.find()
for r in results:
    print(r)


position =  collection.find_one({"imei" : "359769037213334"})

#valor = pst.singleprototest()
#print(valor)
#sv.enviar_proto(valor)

