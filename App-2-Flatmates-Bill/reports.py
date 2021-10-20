from fpdf import FPDF
import webbrowser

class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their names, their due amounts and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("files\house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt= bill.period, border=0, ln=1)

        # Insert name and due amount of 1st flatmate
        pdf.set_font(family="Times", size=12)
        flatmate1_pay = str(round(flatmate1.pays(bill=bill, flatmate2=flatmate2), 2))
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # Insert name and due amount of 2nd flatmate
        flatmate2_pay = str(round(flatmate2.pays(bill=bill, flatmate2=flatmate1), 2))
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        # Saving file
        pdf.output(self.filename)
        webbrowser.open(self.filename)