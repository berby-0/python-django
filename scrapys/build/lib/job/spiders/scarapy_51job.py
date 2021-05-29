import re
import time


import scrapy
from bs4 import BeautifulSoup
from scrapys.job.items import JobItem

date = time.strftime('%Y-%m-%d', time.localtime(time.time()))


class Scarapy51jobSpider(scrapy.Spider):
    name = 'scarapy_51job'
    allowed_domains = ['search.51job.com']

    # 这里初始化这个类,可以动态传值并开始爬虫,这里传的是keyword
    def __init__(self, keyword=None, *args, **kwargs):
        super(Scarapy51jobSpider, self).__init__(*args, **kwargs)
        self.key = re.split('lbl', keyword)
        self.keyword_j =  self.key[1]
        self.start_head = 'https://search.51job.com/list/{},000000,0000,00,9,{},{},2,'.format(self.key[0], self.key[6], self.key[1])
        self.start_tail = '.html?lang=c&postchannel=0000&workyear={}&cotype={}&degreefrom={}&jobterm={}&companysize={}&ord_field=0&dibiaoid=0&line=&welfare=' \
            .format(self.key[3], self.key[4], self.key[2], self.key[7], self.key[5])
        self.start_urls = [self.start_head + '1' +self.start_tail]

        #self.keyword = 'python'

    def parse(self, response):
        res = response
        soup_p = BeautifulSoup(res.text, 'lxml')
        pattern = soup_p.find_all('script')
        p1 = pattern[-1].text
        p2 = p1.replace('\n', '').replace('\r', '').replace('\\', '')
        # 获取当前页面和总页面数
        r1 = re.findall(r'total_page":"([^"]+)"', p2)
        #r2 = re.findall(r'curr_page":"([^"]+)"', p2)
        total = int(r1[0])

        for i in range(1, total + 1):
        #for i in range(1, 2):
            try:
                print('---正在爬取第{}页---'.format(i))
                #url_a = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,' + str(i) + '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
                url_a = (self.start_head + str(i) + self.start_tail)
                yield scrapy.Request(url_a,callback=self.parse_all)

            except:
                print('---第{}页爬取失败---'.format(i))


    def parse_all(self,response):
        res = response
        soup_p = BeautifulSoup(res.text, 'lxml')
        pattern = soup_p.find_all('script')

        p1 = pattern[-1].text
        p2 = p1.replace('\n', '').replace('\r', '').replace('\\', '')
        soup_p2 = BeautifulSoup(p2, 'lxml')
        res2 = re.findall(r'}],"jobid_count":"([^"]+)"', p2)
        p3 = soup_p2.p.text.replace('}],"jobid_count":"' + res2[0] + '","banner_ads":"', '}}').replace('window.__SEARCH_RESULT__ = {"top_ads":[],"auction_ads":[],"market_ads":[],"engine_search_result":[','')
        p6 = p3.replace('}', '}|').replace('}|}|', '}')
        p6 = p6.split('|,')
        items = JobItem()
        print('jjjj',p6)
        for j in p6:
            r = eval(j)
            items['jobid'] = r['jobid']
            items['coid'] = r['coid']
            items['job_href'] = r['job_href']
            items['job_name'] = r['job_name']
            items['keyword'] = self.keyword_j
            items['company_name'] = r['company_name']
            items['providesalary_text'] = r['providesalary_text']
            items['workarea_text'] = r['workarea_text']
            items['companytype_text'] = r['companytype_text']
            items['degreefrom'] = r['degreefrom']
            items['workyear'] = r['workyear']
            items['jobwelf_list'] = r['jobwelf_list']
            items['attribute_text'] = r['attribute_text']
            items['companysize_text'] = r['companysize_text']
            items['companyind_text'] = r['companyind_text']
            items['date1'] = date

            yield items

