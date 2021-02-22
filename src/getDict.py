from os.path import exists, isfile
from tika import parser
from utils import find_accident_id, find_id, find_province, find_name, find_city


def get_dict(path: str):
    if (not exists(path)) and (not isfile(path)):
        return None
    raw = parser.from_file(path)["content"]

    # Número de siniestro
    accident_id = find_accident_id(raw)

    # Nombre
    patient_name = find_name(raw)

    # Dni o cuil
    patient_id = find_id(raw)

    # Localidad
    patient_province = find_province(raw)
    patient_city = find_city(raw)
    patient_location = patient_province + ", " + patient_city

    return {
        "accident_id": accident_id,
        "patient_name": patient_name,
        "patient_id": patient_id,
        "patient_location": patient_location
    }
