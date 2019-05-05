import subprocess
import sys
import psutil
import time
import datetime
log_file = '/tmp/MonitorProcess.txt'


def print_process_information(pid):
  p = psutil.Process(pid)
  message = '[!][Add]pid:'+str(p.pid)+'  '+'name:'+p.name()+'  '+'username:'+p.username()+'  '+'status:' + \
    p.status()+'  '+'start_time:' + \
    datetime.datetime.fromtimestamp(p.create_time()).strftime("%H:%M:%S")
  print message
  fp = open(log_file, 'a')
  try:
    message += '\n'
    fp.writelines(message)
  finally:
      fp.close()


def psutil_process():
  pids_1 = psutil.pids()
  time.sleep(2)
  pids_2 = psutil.pids()
  for pid in pids_2:
    if pid in pids_1:
      #print 'ok!'
      pass
    else:
      print_process_information(pid)


def main():
  while 1:
    psutil_process()


if __name__ == "__main__":
  main()
