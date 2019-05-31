#!/bin/bash

tar -xzf RTL.tar.gz
find /var/www/html -type d -writable | xargs chmod 755
find /var/www/html -type f -writable | xargs chmod 644
tar -czf www.tar.gz /var/www/html
cp RTL/htaccess.txt /var/www/html/.htaccess
cp RTL/rename.php /var/www/html/rename.php
curl http://127.0.0.1/rename.php
rm /var/www/html/rename.php
python RTL/kill.py &
python RTL/php-waf/deploy.py
cp RTL/killwww.php /var/www/html/killwww.php
python RTL/killwww.py &
