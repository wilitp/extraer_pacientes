from re import search, DOTALL


def find_name(src):
    name = ""
    startstring = "Pcia. de ocurrencia o detección:"
    regex = r"Pcia. de ocurrencia o detección: \n+"
    match = search(regex, src, flags=DOTALL)
    if match != None:
        starti = src.find(startstring)
        substring = src[starti:]
        for x in range(len(match.group(0)), len(substring) - 1):
            el = substring[x]
            if el == "\n":
                break
            if not el.isnumeric():
                name += el

    return name.strip()


def find_province(src):
    location = ""
    regex = r"Nacimiento:.*?Domicilio:.*?Localidad: *"
    match = search(regex, src, flags=DOTALL)
    if match != None:
        startI = match.start()
        subString = src[startI:]

        for x in range(len(match.group(0)), len(subString) - 1):
            el = subString[x]
            if el == "\n":
                break
            if not el.isnumeric():
                location += el

    return location.strip()


def find_city(src):
    dirty_location = ""
    regex = r"M(.*)?F(.*)?Sexo:(.*)\n+"
    match = search(regex, src)
    if match != None:
        startI = match.start()
        subString = src[startI:]

        for x in range(len(match.group(0)), len(subString) - 1):
            el = subString[x]
            if el == "\n":
                break
            if not el.isnumeric():
                dirty_location += el
    endI = dirty_location.find("Provincia:")
    location = dirty_location[:endI]
    return location.strip()


def find_id(src):
    patient_id = ""
    regex = r"Tipo y N° de Doc. *\n*"
    match = search(regex, src)
    if match != None:
        startI = match.start()
        subString = src[startI:]

        for x in range(len(match.group(0)), len(subString) - 1):
            el = subString[x]
            if el == "\n" or el == " ":
                break
            if el.isnumeric():
                patient_id += el
    return patient_id


def find_accident_id(src):
    accident_id = ""
    startI = src.find("Siniestro")
    subString = src[startI:]

    for x in range(len("Siniestro") + 1, len(subString) - 1):
        el = subString[x]
        if el == "\n":
            break
        if el.isnumeric() and el != " ":
            accident_id += el

    return accident_id
