# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

'''
self.list.append([r['jobid'], r['coid'], r['job_href'], r['job_name'], r['job_title'], r['company_href'],
                  r['company_name'], r['providesalary_text'], r['workarea_text'], r['companytype_text'],
                  r['degreefrom'], r['workyear'], r['issuedate'], r['jobwelf'], r['jobwelf_list'],
                  r['attribute_text'], r['companysize_text'], r['companyind_text']])
'''


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobid = scrapy.Field()
    coid = scrapy.Field()
    job_href = scrapy.Field()
    job_name = scrapy.Field()
    keyword = scrapy.Field()
    company_name = scrapy.Field()
    providesalary_text = scrapy.Field()
    workarea_text = scrapy.Field()
    companytype_text = scrapy.Field()
    degreefrom = scrapy.Field()
    workyear = scrapy.Field()
    jobwelf_list = scrapy.Field()
    attribute_text = scrapy.Field()
    companysize_text = scrapy.Field()
    companyind_text = scrapy.Field()
    date1 = scrapy.Field()
