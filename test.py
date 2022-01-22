import glob
import os

from fpdf import FPDF
from fuck_3 import getTextFile


arr_q = [f for f in glob.glob("files*.jpeg")]
arr_text = [f for f in glob.glob("files*.jpeg.txt")]
sort = sorted(arr_q)
link = r"C:/prog/pythonPr/"
file_path = r"C:/prog/pythonPr/files1.jpeg.txt"
pdf = FPDF()
pdf.set_font("Arial", size=12)


for f_two in arr_q:
    pdf.add_page()
    print(f_two)
    txt_rename = f"{f_two}.txt"
    print(txt_rename)
    pdf.set_font("Arial", size=12)
    pdf.image(f_two, w=210, x=35, y=20)
    pdf.cell(220, 10, getTextFile(txt_rename), 10)
pdf.output("simple_demo.pdf")

# qqq = f"txt{getTextFile(file_path)}{2*2}"
# print(qqq)