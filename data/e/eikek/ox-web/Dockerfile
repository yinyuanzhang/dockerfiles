FROM eikek/ox-common

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

RUN a2enmod proxy proxy_http proxy_balancer expires deflate headers rewrite mime setenvif lbmethod_byrequests
RUN a2enmod ssl

EXPOSE 80

RUN rm /etc/apache2/sites-enabled/000-default.conf

ADD default /etc/apache2/sites-available/default
ADD proxy_http.conf /etc/apache2/conf-available/proxy_http.conf

RUN /bin/ln -sf ../sites-available/default /etc/apache2/sites-enabled/002-default.conf
RUN /bin/ln -sf ../conf-available/proxy_http.conf /etc/apache2/conf-enabled/proxy_http.conf

WORKDIR /
ADD oxweb ./
RUN chmod a+x oxweb
CMD ["/oxweb"]
