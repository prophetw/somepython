#coding:UTF-8
from openpyxl import load_workbook
from pprint import pprint

# generate json from .xlsx
# https://openpyxl.readthedocs.io/en/stable/tutorial.html#loading-from-a-file
wb = load_workbook(filename='./1.xlsx')

# eg
# B列 tools key  keyColumn='B'
# D列 page title pageTitleColumn = 'D'
# E列 meta description metaDescriptionColumn = "E"
# pageTitle metaDescription metaTitle  seoPara

sheetName = str(' Page title 和 Meta Description ')
keyColumn = 'B'
pageTitleColumn = 'D'
metaDescriptionColumn = "E"
ws = wb[sheetName]

# 提供的key 和 翻译文件的key
keyMap={
    "PDF to Word" : "PDF2Word",
    "PDF to Excel":"PDF2Excel",
    "PDF to PPT":"PDF2PPT",
    "PDF to Image":"PDF2Image",
    "PDF to Text":"PDF2Text",
    "PDF to HTML":"PDF2HTML",
    "Word  to PDF":"Word2PDF",
    "Excel  to PDF":"Excel2PDF",
    "PPT to PDF":"PPT2PDF",
    "Image to PDF":"Image2PDF",
    "HTML to PDF":"HTML2PDF",
    "Text to PDF":"Text2PDF",
    "Merge PDF":"MergePDF",
    "Watermark PDF":"Watermark",
    "Compress PDF": "CompressPDF",
    "Split PDF":"SplitPDF",
    "PDF Organizer":"PageOrganizer",
    "Redact PDF":"RedactPDF",
    "Flatten PDF":"FlattenPDF",
    "PDF Header Footer":"HeaderFooter",
    "Password protect PDF":"PasswordProtect",
    "PDF to cPDF":"PDF2CPDF",
    "Foxit Drive":"Foxit_Drive",
    "phantom pdf online":"PhantomPDF_Online",
    "Foxit Online":"Foxit_Online"
}

# 遍历30行足够了
rowNumber = range(1, 30)

# 输出对象
pageTitleEn = {}
pageTitleZh = {}
metaDescriptionEn = {}
metaDescriptionZh = {}

for index in rowNumber:
    if ws[keyColumn+str(index)].value != None and keyMap.get(ws[keyColumn+str(index)].value) != None:
        key = keyMap[ws[keyColumn+str(index)].value]
        pageTitleEn[key] = ws[pageTitleColumn + str(index)].value.split('\n')[0]
        pageTitleZh[key] = ws[pageTitleColumn + str(index)].value.split('\n')[1]
        metaDescriptionEn[key] = ws[metaDescriptionColumn + str(index)].value.split('\n')[0]
        metaDescriptionZh[key] = ws[metaDescriptionColumn + str(index)].value.split('\n')[1]
pprint(pageTitleEn,width=999)
pprint(metaDescriptionEn,width=999)

pprint(pageTitleZh)
pprint(metaDescriptionZh,width=999)

