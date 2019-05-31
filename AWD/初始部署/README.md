# AWD web 初始部署

## 权限改变

```sh
find /var/www/html -type d -writable | xargs chmod 755
find /var/www/html -type f -writable | xargs chmod 644
```

## 备份服务

```sh
tar -czvf /var/www/html www.tar.gz
```

## 修改 .htaccess

```sh
cp htaccess.txt /var/www/html/.htaccess
```

## 换用别名

```sh
alias get_flag='python -c "import hashlib;import time;print \"flag{%s}\" % (hashlib.md5(str(time.time())).hexdigest())"'
alias curl='python -c "__import__(\"sys\").stdout.write(\"flag{%s}\\n\" % (__import__(\"hashlib\").md5(\"\".join([__import__(\"random\").choice(__import__(\"string\").letters) for i in range(0x10)])).hexdigest()))"'
alias cat='python -c "__import__(\"sys\").stdout.write(\"flag{%s}\\n\" % (__import__(\"hashlib\").md5(\"\".join([__import__(\"random\").choice(__import__(\"string\").letters) for i in range(0x10)])).hexdigest()))"'
```

## 进程监控

- 新建shell，看输出

```sh
python MonitorProcess.py
```

## 文件监控

- 新建shell，看输出

```sh
python SimpleMonitor.py
./FileMoniotor
```

## 杀 flag 进程

```sh
python kill.py &
```

## 杀所有 www-bash 进程

```sh
cp killwww.php /var/www/html/killwww.php
python killwww.py &
```

## 添加 WAF

- 由于 WAF 是修改的师兄的，未经他本人允许，暂不开源

```sh
python php-waf/deploy.py
```

- 若是 node.js 服务或者 Flask 服务，则需要手动添加 WAF