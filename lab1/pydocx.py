import zipfile
from xml.dom import minidom
from docx import Document

# 用python-docx提取作者、创建时间和标题
doc = Document('test.docx')
core_properties = doc.core_properties

# 由于python-docx没有提供对Properties的读写API，
# 只能将docx文件视为压缩包进行处理了
zip_file = zipfile.ZipFile('test.docx')

#组织属于Properties，存放在app.xml中
with zip_file.open('docProps/app.xml') as file:
    # 输出文件内容
    xml_file = minidom.parse(file)
    # 获取Company节点内容
    root = xml_file.documentElement
    company_node = root.getElementsByTagName("Company")[0]
    company_content = company_node.firstChild.data

# 追加到douban.txt中
f = open('douban.txt', 'a', encoding='UTF-8')
f.write('作者:' + str(core_properties.author) + '\n')
f.write('创建时间:' + str(core_properties.created) + '\n')
f.write('标题:' + str(core_properties.title) + '\n')
for para in doc.paragraphs:
    f.write("正文:" + str(para.text) + '\n')
f.write("单位是:" + str(company_content) + '\n')
f.close()