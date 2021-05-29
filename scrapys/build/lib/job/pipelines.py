# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import time
import pymysql


date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

class JobPipeline:
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('localhost', 'root', '123456','51job_a',charset='utf8')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
                insert into app01_custom(jobid,job_href,coid,job_name,keyword,companytype_text,jobwelf_list,degreefrom,
                        company_name,attribute_text,workyear,companysize_text,companyind_text,providesalary_text,
                        workarea_text,date1)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

        # 执行插入数据到数据库操作
        self.cursor.execute(insert_sql, (item['jobid'], item['job_href'], item['coid'], item['job_name'], item['keyword'],
                                 item['companytype_text'], str(item['jobwelf_list']), item['degreefrom'],
                                 item['company_name'], str(item['attribute_text']), item['workyear'],item['companysize_text'],
                                 item['companyind_text'], item['providesalary_text'], item['workarea_text'], item['date1']))

        # 提交，不进行提交无法保存到数据库
        self.conn.commit()

        '''


        models.custom.objects.create(jobid=item['jobid'],job_href=item['job_href'],coid=item['coid'],job_name=item['job_name'],
                                     keyword=item['keyword'],companytype_text=item['companytype_text'],jobwelf_list=str(item['jobwelf_list']),degreefrom=item['degreefrom'],
                                     company_name=item['company_name'],attribute_text=str(item['attribute_text']),workyear=item['workyear'],companysize_text=item['companysize_text'],
                                     companyind_text=item['companyind_text'],providesalary_text=item['providesalary_text'],workarea_text=item['workarea_text'],date1=item['date1'])
        '''

    def close_spider(self, spider):
        #关闭游标和连接
        self.cursor.close()
        self.conn.close()