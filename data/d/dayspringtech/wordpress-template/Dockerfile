FROM amazonlinux:2
RUN amazon-linux-extras install php7.2 -y
RUN yum install mod_php -y

EXPOSE 80

#VOLUME ["/var/www/html"]

COPY wordpress/ /var/www/html/

CMD ["httpd", "-DFOREGROUND"]
