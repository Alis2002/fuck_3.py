import glob
import os
import glob
from fpdf import FPDF
from fuck_3 import getTextFile
from PIL import Image
import os
import posixpath

# header_footer.py

from fpdf import FPDF

path =r'C:/prog/pythonPr/cat/C074 Славянский бульвар/'
ware_image = r"C:/prog/pythonPr/wave.png"

class CustomPDF(FPDF):

    def footer(self):
        self.set_y(-10)

        self.set_font('Arial', 'I', 8)

        # Add a page number
        page =str(self.page_no())
        self.cell(0, 10, page, 0, 0, 'C')


def create_pdf(pdf_path):
    arr_q = [f for f in glob.glob(path + 'Кожух/foto*.jpg')]
    arr_qr = [f for f in glob.glob(path + 'Матрица/foto*.jpg')]
    t_op = open(path + 'text.txt', 'r', encoding='utf-8')
    pdf = CustomPDF(orientation='l')


    pdf.output(pdf_path)

if __name__ == '__main__':
    create_pdf('header_footer.pdf')


# path = "C:/prog/pythonPr/cat/C074 Славянский бульвар/"
# from PIL import Image
# im = Image.open(path +"title_on.jpg")
# (w,h) = im.size
# print(w,h)
# # width=ширина
#
# if (w > h):
#     print("yes")
# else:
#     print("no")
#


# # def path_dir(path):
# def replace_path(aaaaa):
#
#     aaaaa.replace("s", "Q")
#     return aaaaa
#
# print(replace_path("C:\\sfds/"))
#
#
# local = "/cat"
# for lis_one in os.listdir(r"C:/prog/pythonPr/cat/"):
#     path = r"C:/prog/pythonPr/cat/" + lis_one
#     # print(os.getcwd())
#     # print(path)
#
#     # path_path = f"{path}{for lis_two in os.listdir(path):}"
#     # arr_q = [f for f in glob.glob(path + '/files*.jpeg')]
#     # print(arr_q)
#     pdf = FPDF(orientation='l')
#
#     for lis_two in os.listdir(path):
#         sum_path = (f"{path + '/'}" + lis_two)
#         # print(sum_path)
#         arr_q = [f for f in glob.glob(sum_path + '/files*.jpeg')]
#
#
#         # print(arr_q)
#         # pdf.add_page()
#         # pdf.image(arr_q, w=300, x=0, y=0)
#
# #
# #     if os.path.exists(path):
# #
# #
# #
# #         for lis_two in os.listdir(path):
# #         # os.mkdir(g2 + "test", mode=0o777, dir_fd=None)
# #             sum_path = (f"{path + '/'}" + lis_two)
# #             # print(sum_path)
# #
# #             # os.mkdir(os.mkdir(sum_path + "test", mode=0o777, dir_fd=None))
# #             # print(sum_path)
# #
# #
# # #         xu = (f"{path+'/'}"+ g2)
# # #         # print(xu)
# # #         for xui in os.listdir(xu):
# # #             g = xu+"/"+xui
# # #             # print(g)
# # # # for dirs, folder, files in os.walk(path):
# # #    d_p = dirs
# # #    # print(d_p)
# # #    arr_q = [f for f in glob.glob(d_p + '/files*.jpeg')]
# # #    arr_qr = [f for f in glob.glob(d_p + '/foto*.jpg')]
# #    # print(arr_q)
#
