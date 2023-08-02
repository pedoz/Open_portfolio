from fpdf import FPDF

class PDF(FPDF):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    def header(self):
        self.image('../cs50/aula_8/atividades/shirtificate/shirtificate.png', w = pdf.epw, y = 60)
        self.set_font("helvetica", "B", 50)
        self.cell(0, 20, "CS50 Shirtificate", align="C")
        self.ln(110)


pdf = PDF()
pdf.add_page()
name = input("What's your name?").rstrip()
try:
    first, last = name.split(" ")
except ValueError:
    print('Only 2 names allowed')
texto = ' took CS50'
printed = name + texto
pdf.set_font("Times", size=25)
pdf.set_text_color(255,255,255)
pdf.cell(0, 0, printed.title(), align = 'c')
pdf.output(first[0]+last+'.pdf')