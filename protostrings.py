import zenbus_pb2 as zpb2
from google.protobuf.json_format import MessageToJson

def singleprototest():
    """Solo test"""
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
    """
    provpost: 
    value:
    """
    position = provpost.pos.add()
    position.latitude = value["position"]["coordinates"][0]
    position.longitude = value["position"]["coordinates"][1]
    position.utc_millis = int(value["hora"].timestamp() * 1000)
    return provpost

def decode_one_pos_forpad(unic_pos_pad):
    """Envio solo una posicion"""
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = unic_pos_pad["padron"]
    provpost = add_pos(provpost, unic_pos_pad)
    return provpost.SerializeToString()

def decode_pos_forpad(posiciones_pad):
    """Envio multiples posiciones de un solo agente productor"""
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = posiciones_pad[0]["padron"]
    provpost.vehicle_id = posiciones_pad[0]["unidad"]
    for pos in posiciones_pad:
        add_pos(provpost, pos)
    return provpost.SerializeToString()

def add_vehicle(provpost, single_document):
    """asigna los campos del vehiculo donde deberian segun solo un json"""
    provpost.vehicle .vehicle_id = single_document["unidad"]
    provpost.vehicle .license_plate = single_document["placa"]
    provpost.vehicle .label = single_document["imei"]
    return provpost

def add_obj_vehicle(single_document):
    """asigna los campos del vehiculo donde deberian segun solo un json"""
    vehicle = zpb2.Vehicle()
    vehicle.vehicle_id = single_document["unidad"]
    vehicle.license_plate = single_document["placa"]
    vehicle.label = single_document["imei"]
    return vehicle

def decode_pos_forunit(posiciones_unit):
    """Envio multiples posiciones de un solo agente productor"""
    provpost = zpb2.SingleProviderPost()
    provpost.provider_id = posiciones_unit[0]["unidad"]

    # provpost.vehicle.CopyFrom(add_obj_vehicle(posiciones_unit[0]))

    provpost = add_vehicle(provpost, posiciones_unit[0])

    """
    provpost.vehicle.vehicle_id = posiciones_unit[0]["padron"]
    provpost.vehicle.license_plate = posiciones_unit[0]["placa"]
    provpost.vehicle.label = posiciones_unit[0]["imei"]
    """

    for pos in posiciones_unit:
        add_pos(provpost, pos)
    return provpost.SerializeToString()
