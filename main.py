
# импорты
import glob
from fpdf import FPDF
from fuck_3 import getTextFile
from PIL import Image
import os
# глоб ищем файлы

# пути
from test import CustomPDF

path =r'C:/prog/pythonPr/cat/C073 Маяковская/'
ware_image = r"C:/prog/pythonPr/wave.png"


arr_q = [f for f in glob.glob(path + 'Кожух/foto*.jpg')]
# arr_q = [f for f in glob.glob(path + 'Матрица/foto*.jpg')]
# кожух
f = path + "title_two.jpg"
# # матрица
# f = path + "title_three.jpg"

# сортируем
sort = sorted(arr_q)
counter = 0
class CustomPDF(FPDF):

    def footer(self):
        self.set_y(-10)

        self.set_font('Arial', 'I', 10)

        # Add a page number
        page =-1+self.page_no()
        print(page)
        if page > 0:
            self.cell(0, 10, str(page), 0, 0, 'C')


# ориентация текст кодировка
t_op = open(path + 'text.txt', 'r', encoding='utf-8')
pdf = CustomPDF(orientation='l')



# титульный лист
pdf.add_page()
pdf.add_font('DejaVu', "B", 'PTSansRegular.ttf', uni=True)
pdf.set_font('DejaVu', "B",40 )
pdf.image(ware_image, w=300, x=0, y=0)
# pdf.set_fill_color(128)
print(t_op.readline())
pdf.cell(280,50, "Отчёт о состоянии кожуха на станции:", align='C', ln=2)
pdf.multi_cell(280,0, t_op.readline().strip(), align='C')
pdf.image(path + 'title_on.jpg', w=200, x=50, y=80)

pdf.add_font('DejaVu', "B", 'PTSansRegular.ttf', uni=True)
pdf.set_font('DejaVu', 'B', 20)

# второй лист

im = Image.open(f)
(w, h) = im.size
print(w, h)
if (w > h):
    pdf.add_page(orientation='l')
    counter = counter+1
    pdf.image(ware_image, w=300, x=0, y=0)
    pdf.image(f, w=275, x=10, y=25)
    pdf.cell(278, 20, "PHOTO " + "#"+str(counter) +" | " + t_op.readline().strip(),ln=2)
else:
    pdf.add_page(orientation='P')
    counter = counter + 1
    pdf.image(ware_image, w=220, x=0, y=0)
    # неформал
    pdf.image(f, w=135, x=43, y=30)
    # стандарт
    # pdf.image(f, w=145, x=35, y=30)
    pdf.cell(278, 20, "PHOTO " + "#" + str(counter) + " | " + t_op.readline().strip(), ln=2)

# функция на первую папку
for f_two in arr_q:
    im = Image.open(f_two)
    (w, h) = im.size
    print(w, h)
    # width=ширинa
    if (w > h):
        pdf.add_page(orientation='l')#длина
        counter = counter + 1
        txt_renam = f"{f_two}.txt"
        # pdf.set_fill_color(128)
        pdf.cell(278, 20, "PHOTO " + "#"+ str(counter) +" | "+ getTextFile(txt_renam), ln=2)
        # pdf.image(f_two, w=200, x=25, y=30) ширина
        pdf.image(f_two, w=280, x=10, y=25)  # высота
        pdf.image(ware_image, w=300, x=0, y=0)
        pdf.multi_cell(270, 140, '', 0, 0)
        pdf.multi_cell(270, 10, align="R")

    else:
        counter = counter + 1
        pdf.add_page(orientation='P')
        txt_rename = f"{f_two}.txt"
        # pdf.set_fill_color(128)
        g = os.path.exists(txt_rename)
        if g:
            pdf.cell(190, 20, "PHOTO " + "#"+str(counter) +" | "+ getTextFile(txt_rename), ln=2)
        else:
            pdf.cell(190, 20, "PHOTO " + "#"+str(counter), ln=2)
        # pdf.image(f_two, w=145, x=35, y=30)
        # высота стандарт
        pdf.image(f_two, w=118, x=50, y=30)
        # # неформал
        pdf.image(ware_image, w=220, x=0, y=0)
        # pdf.set_fill_color(50, 80 ,90)
        pdf.multi_cell(190, 230, '', 0, 0, fill=False)
        # pdf.set_fill_color(50, 189, 90)


# печать
test_data = open(path + 'text.txt', 'r', encoding='utf-8').readline().strip()
test_test_data = test_data.strip()
# out = (f"{test_test_data} матрица.pdf")
out = (f"{test_test_data} кожух.pdf")
pdf.output(out)

