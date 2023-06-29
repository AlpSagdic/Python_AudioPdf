import sys
import requests
from PyPDF2 import PdfReader

#Constants
API_KEY = "a7949fecb85043bcb1f389162b7a9868"
ENDPOINT = "https://api.voicerss.org/?"
LANGUAGE = "tr-tr"
VOICE = "MP3"
TEXT = ""

text_form = input("What's your text form (pdf/text): ").lower()

#To read the pdf
if text_form == "pdf":
    pdf_path = input("What's your pdf name (such as example.pdf):")
    with open(f"{pdf_path}", "rb") as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            page_text = page.extract_text()
            TEXT = page_text

#To read the text
elif text_form == "text":
    text = input("What's your text: ")
    TEXT = text

else:
    print("Wrong input!")
    sys.exit()

#Voice RSS parameters
parameters = {
    "key": API_KEY,
    "src": TEXT,
    "hl": LANGUAGE,
    "c": VOICE
}

response = requests.post(url=ENDPOINT, params=parameters)

if response.status_code == 200:
    print(f"You can find your voiced text here: {response.url}")
else:
    print(f"You have a problem {response.reason}")
