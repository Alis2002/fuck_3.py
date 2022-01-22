import glob
from fpdf import FPDF
from fuck_3 import getTextFile


arr_q = [f for f in glob.glob("files*.jpeg")]
arr_text = [f for f in glob.glob("files*.jpeg.txt")]
sort = sorted(arr_q)
counter = 0


ware_image = r"C:/prog/pythonPr/wave.png"
link = r"C:/prog/pythonPr/"
file_path = r"C:/prog/pythonPr/files1.jpeg.txt"


pdf = FPDF(orientation='l')
pdf.set_font("Arial", size=20)
pdf.add_page()
pdf.image(ware_image, w=300, x=0, y=0)
pdf.cell(270, 140, 'Ghtpt', align="C")

for f_two in arr_q:
    counter = counter+1
    pdf.add_page()
    print(f_two)
    txt_rename = f"{f_two}.txt"
    print(txt_rename)
    pdf.set_fill_color(128)
    pdf.cell(278, 20, getTextFile(txt_rename), align='C', ln=2)
    pdf.image(f_two, w=249, x=25, y=30)
    pdf.image(ware_image, w=300, x=0, y=0)
    pdf.multi_cell(270, 140, '', 0, 0)
    pdf.multi_cell(270, 10, str(counter), align="R")
    # pdf.cell(278, 159, "1", align='J')
    # pdf.set_fill_color(128)
pdf.output("simple_demo.pdf")

