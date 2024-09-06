import PyPDF2
from docx import Document
from docxtpl import DocxTemplate # generating template with docxtpl



# FOR PDF FILES
def extract_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

pdf_text = extract_pdf('your_pdf.pdf')
print(pdf_text)


# FOR WORD FILES
def extract_word(docx_file_path):
    doc = Document(docx_file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

word_text = extract_word('your_docx.docx')
print(word_text)




def generate_template(template_path, output_path, context):
    doc = DocxTemplate(template_path)
    doc.render(context)
    doc.save(output_path)

# the context for the template
context = {
    'title': 'Document Title',
    'section_heading': 'Introduction',
    'content': 'This is the populated content for the section.'
}

generate_template('template.docx', 'output.docx', context)