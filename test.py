import glob
from fpdf import FPDF
import os.path
import sys
from fuck_3 import getTextFile

local_link = r"C:/prog/quest/text.xt"
print(getTextFile(local_link))
pdf = FPDF(orientation='l', format='A4')
pdf.set_font('Times')

fos_ware = r"C:\prog\PDF\wave.PNG"
arr_q = [f for f in glob.glob("files*.jpeg")]
text_sorted = sorted([f for f in glob.glob("files*jpeg.txt")])
ware = r"C:/prog/quest/"
for x in text_sorted:
    a = ware + x
print(a)



sort = sorted(arr_q)

for image_file in sort:
    pdf.add_page()
    pdf.image(fos_ware, w=210, x=0, y=0)
    pdf.image(image_file, w=190, x=35, y=20)

pdf.output("image.pdf")
