import requests
from selenium import webdriver
import re
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("http://www.tennisabstract.com/cgi-bin/player.cgi?p=RogerFederer")
x=driver.find_element_by_css_selector('span.likelink')
x.click()
y=driver.find_element_by_xpath('//*[@id="splitsbody"]/tr[12]/td[1]/span')
y.click()
th=driver.find_element_by_tag_name('thead')
headers=th.text
data={}
yr=2018
for i in range(1,11):
    yr=yr-1
    d=driver.find_element_by_xpath('//tr[@id="sA{}"]'.format(i))
    data[yr]=d.text


ace=headers.split(" ").index('Ace%')
rpw=headers.split(" ").index('RPW')
spw=headers.split(" ").index('SPW')
bias=2
ace_avg=0
rpw_avg=0
spw_avg=0

for key in data.keys():
    print "Ace %age ,year :{} {}".format(key,re.findall(r'\d+.\d+',data[key].split(" ")[ace+bias])[0])
    print "rpw %age ,year :{} {}".format(key,re.findall(r'\d+.\d+',data[key].split(" ")[rpw+bias])[0])
    print "spw %age ,year :{} {}".format(key,re.findall(r'\d+.\d+',data[key].split(" ")[spw+bias])[0])
    ace_avg+=float(re.findall(r'\d+.\d+',data[key].split(" ")[ace+bias])[0])
    rpw_avg+=float(re.findall(r'\d+.\d+',data[key].split(" ")[rpw+bias])[0])
    spw_avg+=float(re.findall(r'\d+.\d+',data[key].split(" ")[spw+bias])[0])
    print "\n \n \n"

print "Ace percentage avg {}".format(ace_avg/len(data))
print "rpw_avg percentage avg {}".format(rpw_avg/len(data))
print "spw_avg percentage avg {}".format(spw_avg/len(data))









