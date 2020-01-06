FROM centos:6.9
RUN yum update -y
RUN yum upgrade -y
RUN yum install httpd mysql telnet vi vim wget rsync ftp ssh mysql-server php-* -y
RUN /etc/rc.d/init.d/httpd start
RUN chown -R apache:apache /var/www/html
RUN /etc/rc.d/init.d/httpd stop
EXPOSE 80 3306
VOLUME ["/var/www/html", "/var/lib/mysql", "/etc/httpd/logs"]
COPY start.sh /start.sh
CMD ["./start.sh"]

