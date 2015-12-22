__author__ = 'manh-ha'
import urllib2
import url
from bs4 import BeautifulSoup
import socket


class data_fetch:
    def __init__(self):
        self.url_pre="http://panelhargabkp.pertanian.go.id/?"
        self.para=['search','pedagang','kd_prop','kd_kab','komoditas','periode','minggu','bulan','tahun','minggu1','bulan2','tahun1','batas','submit']
        self.p_value=['hargapedagang','G','11','','','mingguan','1','04','2015','5','04','2015','100','1']
        self.url=''
        self.respond=''
        self.datasets=''
        self.headings=''
        self.source=''
        socket.setdefaulttimeout(3600)
    def set_price_type(self,type):
        if type=='SALE':
            self.p_value[self.para.index('pedagang')]='G'
        if type=='RETAIL':
            self.p_value[self.para.index('pedagang')]='E'

    def set_month(self,month):
        self.p_value[self.para.index('bulan')]=month
        self.p_value[self.para.index('bulan2')]=month

    def set_year(self,year):
        self.p_value[self.para.index('tahun')]=year
        self.p_value[self.para.index('tahun1')]=year

    def set_province(self,province):
        self.p_value[self.para.index('kd_prop')]=province

    def create_url(self):
        self.url=self.url_pre;
        for i in range(0,13):
            self.url+=self.para[i]+'='+self.p_value[i]+'&'
        self.url+=self.para[13]+'='+self.p_value[13]

    def get(self):
        req=urllib2.Request(self.url)
        #req=url.urlopen_with_retry(self.url)
        req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
        #self.response = urllib2.urlopen(req)
        self.response=url.urlopen_with_retry(req)
        self.source=self.response.read()
        #self.source=open('data.html', 'r')
        print self.url

    def parser(self):
        soup = BeautifulSoup(self.source,"html.parser")
        table = soup.find("table", attrs={"class":"responsive"})
        # The first tr contains the field names.
        self.headings = [th.get_text() for th in table.find("tr").find_all("th")]
        self.datasets = []
        for row in table.find_all("tr")[1:]:
            #dataset = zip(headings, (td.get_text() for td in row.find_all("td")))
            dataset=[]
            for td in row.find_all("td"):
                dataset.append(td.get_text())
            self.datasets.append(dataset)
    def getdata(self,province,month,year,type):
        self.set_province(province)
        self.set_month(month)
        self.set_year(year)
        self.set_price_type(type)
        self.create_url()
        self.get()
        self.parser()
