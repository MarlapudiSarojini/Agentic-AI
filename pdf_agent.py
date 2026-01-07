from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(report_text):
    file_name = "weather_report.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)
    text = c.beginText(40, 750)

    for line in report_text.split(". "):
        text.textLine(line)

    c.drawText(text)
    c.save()

    return file_name
