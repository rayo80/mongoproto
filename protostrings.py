import zenbus_pb2 as zpb2

def singleprototest():
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = 1234
    position = provpost.pos.add()
    position.latitude = 48.8584
    position.longitude = 2.2945
    position.utc_millis = 1234567890123

    valor = provpost.SerializeToString()
    return valor