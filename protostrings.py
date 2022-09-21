import zenbus_pb2 as zpb2
from google.protobuf.json_format import MessageToJson

def singleprototest():
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = 1234
    position = provpost.pos.add()
    position.latitude = 48.8584
    position.longitude = 2.2945
    position.utc_millis = 1234567890123
    valor = provpost.SerializeToString()
    return valor

def double_prototest():
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = 123456
    position = provpost.pos.add()
    position.latitude = 0.123456
    position.longitude = 12.345678
    position.utc_millis = 1642584629991
    position1 = provpost.pos.add()
    position1.latitude = 0.123456
    position1.longitude = 12.345683
    position1.utc_millis = 1642584630000
    print(MessageToJson(provpost))
    valor = provpost.SerializeToString()
    return valor

def add_pos(provpost, value):
    position = provpost.pos.add()
    position.latitude = value["position"]["coordinates"][0]
    position.longitude = value["position"]["coordinates"][1]
    position.utc_millis = int(value["hora"].timestamp() * 1000)
    return provpost


def singleprotodatatest(value):
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = value["unidad"]
    provpost = add_pos(provpost, value)
    valor = provpost.SerializeToString()
    print(MessageToJson(provpost))
    return valor


def decode_pos_forunit(historical):
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = historical[0]["unidad"]
    for state in historical:
        add_pos(provpost, state)
    print(MessageToJson(provpost))
    valor = provpost.SerializeToString()
    return valor