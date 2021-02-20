import PyPDF2

fullText = ""

with open("../assets/test.pdf", "rb") as fileObj:
    reader = PyPDF2.PdfFileReader(fileObj)
    numPages = reader.getNumPages()
    for x in range(numPages - 1):
        pageObj = reader.getPage(x)
        print(pageObj.extractText())
