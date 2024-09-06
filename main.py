import PyPDF2

def extract_pdf_text(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

pdf_text = extract_pdf_text('pdf_word.pdf')
print(pdf_text)