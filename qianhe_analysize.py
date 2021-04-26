import pdfplumber
import pandas as pd
import sys
import importlib

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

# def pdf2text(path, new_name):
#     # 创建一个文档解析器
#     parser = PDFParser(path)
#     # 创建一个PDF文档对象存储文档结构
#     document = PDFDocument(parser)
#     # 判断文件是否允许文本提取
#     if not document.is_extractable:
#         raise PDFTextExtractionNotAllowed
#     else:
#         # 创建一个PDF资源管理器对象来存储资源
#         resmag = PDFResourceManager()
#         # 设定参数进行分析
#         laparams = LAParams()
#         # 创建一个PDF设备对象
#         device = PDFPageAggregator(resmag, laparams=laparams)
#         # 创建一个PDF解释对象
#         interpreter = PDFPageInterpreter(resmag, device)
#         # 处理每一页
#         for page in PDFPage.create_pages(document):
#             interpreter.process_page(page)
#             # 接受该页面的LTPage对象
#             layout = device.get_result()
#             for y in layout:
#                 if (isinstance(y, LTTextBoxHorizontal)):
#                     with open("%s"%(new_name),'a',encoding="utf-8") as f:
#                         f.write(y.get_text()+"\n")
#                         if "code" in y.get_text():
#                             print(y.get_text())

# path = open("D:\\Hansson\\project\\E-METER\\datasheet\\BACnet\\BACstac\\BACstac_32_Data_Sheet.pdf",'rb')
# pdf2text(path, "pdfminer.txt")

findStrList = ['生产量']
filePath = "D:\\Hansson\\others\\stock\\jiangyou\\qianhe\\2020.pdf"

def findStrInTable(targetTable, findStr):
    findFlag = False
    ret = False
    for x in targetTable:
        if findStr in x:
            findFlag = True
            break
    if findFlag == True:
        for x in targetTable:
            print(x, end=" ")
        print(" ")
        findFlag = False
        ret = True
    return ret

pdf = pdfplumber.open(filePath)

# output the total number of pages
print(len(pdf.pages))

i = 0
while i < len(pdf.pages):
    index_page = pdf.pages[i]
    # find the tables list of the i page
    tables = index_page.extract_tables()
    for j in range(0, len(tables)):
        for findstr in findStrList:
            if findStrInTable(tables[j], str(findstr)) == True:
                print("find page nume is ", i)
    i += 1
