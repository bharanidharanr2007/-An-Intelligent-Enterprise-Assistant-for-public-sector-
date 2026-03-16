import PyPDF2
from transformers import pipeline

summarizer = pipeline("summarization")

def extract_text(file):

    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def summarize_document(text):

    summary = summarizer(text[:1000], max_length=120, min_length=40)

    return summary[0]['summary_text']
