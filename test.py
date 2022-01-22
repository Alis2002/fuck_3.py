import glob
from fpdf import FPDF
import os.path
import sys
from fuck_3 import getTextFile


pdf = FPDF(orientation='l', format='A4')
pdf.set_font('Times')

fos_ware = r"C:\prog\pythonPr\wave.PNG"
arr_q = [f for f in glob.glob("files*.jpeg")]
text_sorted = sorted([f for f in glob.glob("files*jpeg.txt")])
ware = r"C:/prog/pythonPr/"
sort = sorted(arr_q)
for x in text_sorted:
    local_link = ware + x
    get_link = (getTextFile(local_link))
    print(local_link)
cent_q = 1




def create_counter():
    i = 0

    def func():
        nonlocal i
        i += 1
        return i

    return func


counter = create_counter()
for image_file in sort:
    pdf.add_page()
    pdf.image(image_file, w=210, x=35, y=20)
    pdf.set_fill_color(173, 255, 47)
    pdf.cell(w=80, h=90, txt='hgvhg', border='T'+'L', ln=2, align='C', fill=True, link='')


    # pdf.image(image_file, w=210, x=35, y=20)
()


pdf.output("image.pdf")
