#!/bin/bash

tar -xzf RTL.tar.gz
find /var/www/html -type d -writable | xargs chmod 755
find /var/www/html -type f -writable | xargs chmod 644
tar -czf www.tar.gz /var/www/html
cp RTL/htaccess.txt /var/www/html/.htaccess
alias get_flag='python -c "import hashlib;import time;print \"flag{%s}\" % (hashlib.md5(str(time.time())).hexdigest())"'
alias curl='python -c "__import__(\"sys\").stdout.write(\"flag{%s}\\n\" % (__import__(\"hashlib\").md5(\"\".join([__import__(\"random\").choice(__import__(\"string\").letters) for i in range(0x10)])).hexdigest()))"'
alias cat='python -c "__import__(\"sys\").stdout.write(\"flag{%s}\\n\" % (__import__(\"hashlib\").md5(\"\".join([__import__(\"random\").choice(__import__(\"string\").letters) for i in range(0x10)])).hexdigest()))"'
python RTL/kill.py &
python RTL/php-waf/deploy.py
cp RTL/killwww.php /var/www/html/killwww.php
python RTL/killwww.py &
