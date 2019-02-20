# -*- coding:utf8 -*-
# Author: RTL
# Date: 2019.02.20

import os

PORT = 9999

def Window(n):
  for i in range(n):
    os.system("gnome-terminal -x nc -lvp %d", PORT)

if __name__ == "__main__":
  Window(3)