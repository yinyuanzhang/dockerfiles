FROM alpine:3.10.2

RUN /sbin/apk add --no-cache php7-apache2 php7-mbstring php7-gd php7-xml php7-xmlrpc php7-soap php7-json php7-pdo php7-mysqlnd php7-intl php7-sqlite3 php7-curl php7-simplexml php7-zip apache2-ssl

RUN /bin/mv /etc/apache2/httpd.conf /etc/apache2/httpd.conf.origin \
&& /bin/sed -e "s/logs\/access\.log/\/dev\/stdout/" -e "s/logs\/error.log/\/dev\/stderr/" -e "s/index\.html/index\.htm index\.html index\.php default\.html/" /etc/apache2/httpd.conf.origin > /etc/apache2/httpd.conf \
&& /bin/mv /etc/apache2/conf.d/ssl.conf /etc/apache2/conf.d/ssl.conf.origin \
&& /bin/sed -e "s/logs\/ssl_access\.log/\/dev\/stdout/g" -e "s/logs\/ssl_error.log/\/dev\/stderr/g" -e "s/logs\/ssl_request\.log/\/dev\/stdout/g" /etc/apache2/conf.d/ssl.conf.origin > /etc/apache2/conf.d/ssl.conf \
&& /bin/echo -e "IndexOptions Charset=UTF-8" >> /etc/apache2/conf.d/autoindex.conf

RUN /bin/mv /var/www/localhost/htdocs/index.html /var/www/localhost/htdocs/default.html

EXPOSE 80 443

CMD ["/usr/sbin/httpd","-DFOREGROUND"]
