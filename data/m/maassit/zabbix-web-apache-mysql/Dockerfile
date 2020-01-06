FROM zabbix/zabbix-web-apache-mysql:alpine-latest
MAINTAINER https://github.com/MaassIT
RUN sed -i -E "s/('de_DE' => \['name' => _\('German \(de_DE\)'\),.+)false(],)/\1true\2/" /usr/share/zabbix/include/locales.inc.php
