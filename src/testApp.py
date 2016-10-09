# -*-coding:utf-8-*-
import urllib, urllib2
import gzip
import StringIO
import logging.handlers
import logging.config
logging.config.fileConfig('config/logging.conf')
# logger = logging.getLogger('root')
# logger = logging.getLogger('simpleExample')
logger = logging.getLogger('rotatingLogger')

class TestA:
    def testLog(self):


        for i in range(1,1000):
            logger.debug("debug message")
            logger.info("info message")
            logger.warn("warn message")
            logger.error("error message")
            logger.critical("critical message")


if __name__ == '__main__':
    # print('请输入您要查询的内容：')
    # txt_1_value = input()
    # url = 'http://epub.cnki.net/kns/brief/default_result.aspx?action=44&mark=&NaviCode=*&ua=1.11&PageName=ASP.brief_default_result_aspx&DbPrefix=SCDB&DbCatalog=中国学术文献网络出版总库&ConfigFile=SCDBINDEX.xml&db_opt=CJFQ%2CCJFN%2CCDFD%2CCMFD%2CCPFD%2CIPFD%2CCCND%2CCCJD%2CHBRD&txt_1_sel=FT%24%25%3D%7C&txt_1_value1=' + txt_1_value + '&txt_1_special1=%25&his=0&parentdb=SCDB&__=Fri%20Jul%2010%202015%2021%3A34%3A32%20GMT%2B0800%20'
    # req = urllib2.Request(url)
    # response = urllib2.urlopen(req)
    # the_page = response.read()
    # print the_page

    for i in range(2,10):
        print i


    t = TestA()
    t.testLog()


    # logger.addHandler()

