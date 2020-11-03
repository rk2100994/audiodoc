# pip install ppttsx3
# pip install PyPDF2
import pyttsx3
import PyPDF2
book = open('doc.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
for num in range(1,pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    # speaker.say("Hey I can talk")
    speaker.runAndWait()