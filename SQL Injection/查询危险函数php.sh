#! /bin/bash

grep -r -n "\(mysql\|mssql|mysql_db\)_query\(.*\$_\(GET\|\POST\) .*\)" src/ | awk -F: '{print "filename: "$1"\nline: "$2"\nmatch: "$3"\n\n"}'

grep -r -n "\(oci\|ora\)_parse\(.*\$_\(GET\|\POST\) .*\)" src/ | awk -F: '{print "filename: "$1"\nline: "$2"\nmatch: "$3"\n\n"}'

grep -r -n "\(odbc_prepare\|odbc_exec\)\(.*\$_\(GET\|\POST\) .*\)" src/ | awk -F: '{print "filename: "$1"\nline: "$2"\nmatch: "$3"\n\n"}'

grep -r -n "mysql_bind\(.*\$_\(GET\|\POST\) .*\)" src/ | awk -F: '{print "filename: "$1"\nline: "$2"\nmatch: "$3"\n\n"}'

