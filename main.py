import PyPDF2
import spacy
import os

pdf_file = open("example.pdf", "rb")

r_pdf = PyPDF2.PdfReader(pdf_file)

numb_pages = r_pdf.numPages

text = ""
for page in range(numb_pages):
    cur_page = r_pdf.getPage(page)
    text_page = cur_page.extractText()
    text += text_page

pdf_file.close()

print(text)

nlp = spacy.load("es_core_news_sm")
doc = nlp(text)

tokens = doc.sents
for token in tokens:
    if token.text in w_libra:
        print(token.text)