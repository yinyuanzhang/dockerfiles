FROM nenadalm/php:latest

RUN yum upgrade -y
RUN yum install -y httpd

RUN rm /etc/httpd/conf.d/welcome.conf
RUN ln /opt/phpfarm/inst/current/bin/php-cgi /var/www/cgi-bin/php-cgi
COPY configuration /

EXPOSE 80

CMD /usr/sbin/apachectl -D FOREGROUND

