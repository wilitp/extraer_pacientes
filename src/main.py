from tika import parser
from utils import findAccidentId, findId, findLocation, findName

# Nombre de paciente - número de siniestro(not available) - federación patronal(bool) - dni / cuil - localidad

raw = parser.from_file("../assets/test.pdf")["content"]

# Número de siniestro
accident_id = findAccidentId(raw)

# Nombre
patient_name = findName(raw)

# Dni o cuil
patient_id = findId(raw)

# Localidad
patient_location = ""

print(patient_id)
