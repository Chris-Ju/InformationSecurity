# -*- coding:utf8 -*-
# Author: Chris
# Date: 2019.02.18


def Encryption(n, e, m):
  return pow(m, e, n)

def Decryption(n, d, c):
  return pow(c, d, n)

if __name__ == "__main__":
  while True:
    chose = raw_input("1.Encryption enter 1\n2.Decryption enter 2\n3.Quit enter 'q'\n>>")
    if chose == '1':
      n = input("Please input n:\n>>")
      e = input("Please input e:\n>>")
      m = input("Please input M:\n>>")
      print Encryption(n, e, m)
    elif chose == '2':
      n = input("Please input n:\n>>")
      d = input("Please input d:\n>>")
      c = input("Please input C:\n>>")
      print Decryption(n, d, c)
    elif chose == 'q':
      break
    else:
      print("Wrong input!\n")



