import PyDf2

pdfFileObj = open('test.pdf' , 'rb')
pdfReader = PyPDF2.PdfileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
data = pageObj.extractText()
print(data)
pdfFileObj.close()