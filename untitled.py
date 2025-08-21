"""Extract text from ``test.pdf`` using PyPDF2."""

import PyPDF2


with open("test.pdf", "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    page_obj = pdf_reader.getPage(0)
    data = page_obj.extractText()
    print(data)
