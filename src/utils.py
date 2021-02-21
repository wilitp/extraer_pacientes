import re


def findName(src):
    name = ""
    startString = "Pcia. de ocurrencia o detección:"
    regex = r"Pcia. de ocurrencia o detección: \n+"
    match = re.search(regex, src)
    startI = src.find(startString)
    subString = src[startI:]

    for x in range(len(match.group(0)), len(subString) - 1):
        el = subString[x]
        if el == "\n":
            break
        if not el.isnumeric():
            name += el

    return name.strip()


def findLocation(src):
    return src


def findId(src):
    return src


def findAccidentId(src):
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
