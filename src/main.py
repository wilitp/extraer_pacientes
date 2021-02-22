from getDict import get_dict
from os import listdir
from datetime import date, timedelta
import pandas as pd

path_to_dir = "../assets"

paths = listdir(path_to_dir)

patient_dicts = []

for path in paths:
    actual_path = path_to_dir + "/" + path
    my_dict = get_dict(actual_path)
    if my_dict != None:
        patient_dicts.append(my_dict)
    pass

accident_ids = []
names = []
ids = []
locations = []

# Lista de aseguradoras de riesgo de trabajo
arts = []

appointment_date = date.today() + timedelta(days=-7)
appointment_dates = []

for patient_dicts in patient_dicts:
    accident_ids.append(patient_dicts["accident_id"])
    names.append(patient_dicts["patient_name"])
    locations.append(patient_dicts["patient_location"])
    ids.append(patient_dicts["patient_id"])
    arts.append("FEDERACION PATRONAL")
    appointment_dates.append(appointment_date.strftime("%d/%m/%Y"))

df = pd.DataFrame({
    "ART": arts,
    "FECHA DE AUDITORIA": appointment_dates,
    "NOMBRE Y APELLIDO DEL PACIENTE": names,
    "SINIESTRO": accident_ids,
    "DNI/CUIT/CUIL": ids,
    "LOCALIDAD/PROVINCIA": locations,
})

df.to_excel("../output/asdf.xlsx", index=False)
