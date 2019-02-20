# -*- coding:utf8 -*-
# Author: RTL
# Date: 2019.02.20


ip = []


import socket
import multiprocessing


def func(cnn):
  while True:
    res = cnn.recv(1024)

if __name__ == '__main__':
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('0.0.0.0', 9999))
  s.listen(5)
  while True:
    try:
      print "Listening..." 
      cnn, addr = s.accept()
      print "Accept from %s" % str(addr)
      m = multiprocessing.Process(target=func, args=(cnn,))
      m.daemon = True 
      m.start()
    except:
      break
