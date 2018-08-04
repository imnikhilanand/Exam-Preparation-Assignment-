





import PyPDF2

f = open('JavaBasics-notes.pdf','rb')

pdf_reader = PyPDF2.PdfFileReader(f)

pages_no = pdf_reader.getNumPages()

str = ""

for x in range(0,pages_no+1):
    page = pdf_reader.getPage(0)
    current_text = page.extractText()
    str = str +" "+ current_text            

str.lower()




words = set(["inheritance","encapsulation","multithreading"])
