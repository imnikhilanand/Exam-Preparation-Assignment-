#importing PyPDF2 for reading PDF file
import PyPDF2

#Opening file
f = open('JavaBasics-notes.pdf','rb')

#pdf_reader object for pdf file operations
pdf_reader = PyPDF2.PdfFileReader(f)

#fetching nuber of pages 
pages_no = pdf_reader.getNumPages()

#creating a string str to append text form all the pages
str = ""

#appending all pages into a single string
for x in range(0,pages_no+1):
    page = pdf_reader.getPage(0)
    current_text = page.extractText()
    str = str +" "+ current_text         
    
#lowercase all the string 
str.lower()

#splitting the string in tokens
new_str = str.split()

#words that should be eliminated from the string
words = set(["inheritance","encapsulation","multithreading"])

#final string that has to be returned 
final = ""

#variables to count the occurance of given keywords
inh=0
en=0
mu=0

#returning the final string
for x in new_str:
    #counting inheritance occurance    
    if x == "inheritance":
        inh=inh+1
    #counting encapsulation occurance
    if x == "encapsulation":
        en=en+1
    #counting multithreading occurance
    if x == "multithreading":
        mu=mu+1
    #removeing the keywords and appending to final string
    if x not in words:
        final = final +" "+ x;
    

#printing the string
print(final)



