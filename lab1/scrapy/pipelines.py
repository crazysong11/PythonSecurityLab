# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface


class PythonSpPipeline:

    def process_item(self, item, spider):
        #获取item中的三部分
        title = item.get('title', '')
        rate = item.get('rate', '')
        inq = item.get('inq', '')
        #写入douban.txt文件中
        f = open('douban.txt', 'a', encoding='UTF-8')
        f.write(str(title) + ',' + str(rate) + ',' + str(inq) + '\n')
        f.close()
        return item
