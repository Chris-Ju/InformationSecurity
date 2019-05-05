#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ** Author: ssooking

import shutil
import os
import argparse
from pyinotify import WatchManager, Notifier,ProcessEvent
from pyinotify import IN_DELETE, IN_CREATE,IN_MOVED_TO,IN_ATTRIB,IN_ACCESS,IN_OPEN,IN_CLOSE_WRITE

bak_path = "/tmp/Liuliang"

class EventHandler(ProcessEvent):
  def __init__(self):
    self.process = ""

  # 创建事件
  def process_IN_CREATE(self, event):
    print "[!] Create : " + event.pathname
    DeleteFileOrDir(event.pathname)

  # 删除事件
  def process_IN_DELETE(self, event):
    print "[!] Delete : " + event.pathname
    recoverFile(event.pathname)

  #文件属性被修改，如chmod、chown命令
  def process_IN_ATTRIB(self, event):
    print "[!] Attribute been modified:" + event.pathname
    if self.process != event.pathname:
        recoverFile(event.pathname)
    self.process = ""

  #文件被移来，如mv、cp命令
  def process_IN_MOVED_TO(self, event):
    print "[!] File or dir been moved to here: " + event.pathname
    DeleteFileOrDir(event.pathname)

  #file in access
  def process_IN_ACCESS(self, event):
    print "[!] File or dir been accessd:" + event.pathname

  # file in close_write
  def process_IN_CLOSE_WRITE(self, event):
    print "[!] File or dir been writed:" + event.pathname
    if self.process != event.pathname:
      recoverFile(event.pathname)
      self.process = event.pathname
  

def DeleteFileOrDir(target):
  if os.path.isdir(target):
    fileslist = os.listdir(target)
    for files in fileslist:
      DeleteFileOrDir(target + "/" + files)
    try:
      os.rmdir(target)
      print "     >>> Delete directory successfully: " + target
    except:
        print "     [-] Delete directory failed: " + target

  if os.path.isfile(target):
    try:
      os.remove(target)
      print "     >>> Delete file successfully" + target
    except:
      print "     [-] Delete file filed:  " + target


def recoverFile(target):
  if os.path.exists(bak_path + target):
    if os.path.isfile(target):
      try:
        shutil.copy(bak_path + target, target)
        print "     >>> recover file successfully: " + target
      except Exception:
        print "     [-] recover file " + target
          


def Monitor(path):
  wm = WatchManager()
  mask = IN_DELETE | IN_CREATE | IN_MOVED_TO | IN_ATTRIB | IN_ACCESS | IN_CLOSE_WRITE
  notifier = Notifier(wm, EventHandler())
  wm.add_watch(path, mask,rec=True)
  print '[+] Now Starting Monitor:  %s'%(path)
  while True:
    try:
      notifier.process_events()
      if notifier.check_events():
        notifier.read_events()
    except KeyboardInterrupt:
      notifier.stop()
      break
                  
if __name__ == "__main__":
  parser = argparse.ArgumentParser(
  usage="%(prog)s -w [path]",
  description=('''
    Introduce：Simple File Monitor!  by ssooking''')
)
parser.add_argument('-w','--watch',action="store",dest="path",default="/var/www/html/",help="directory to watch,default is /var/www/html/")
args=parser.parse_args()
Monitor(args.path)
