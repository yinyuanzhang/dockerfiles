FROM centos:7.5.1804
LABEL	maintainter="rajesh.jonnalagadda@phenompeople.com" \
		version="2.6.2"
EXPOSE 80
RUN groupadd -g 398 icingacmd && \
    groupadd -g 404 icingaweb2 && \
    groupadd -g 405 apache && \
    useradd -g 405 apache -d /usr/share/httpd -s /sbin/nologin 
RUN yum install -y -q --setopt=tsflags=nodocs httpd \
	php71w php71w-cli php71w-devel php71w-pgsql
RUN rpm --import https://packages.icinga.com/icinga.key && \
	yum install -y -q https://packages.icinga.com/epel/icinga-rpm-release-7-latest.noarch.rpm \
	yum install -y -q centos-release-scl
RUN yum install -y -q icingaweb2 icingacli sclo-php71-php-pecl-imagick
ADD files/php.ini /etc/opt/rh/rh-php71/php.ini
COPY files/*.sh /opt/rh/
ADD files/pgsql.schema.sql /usr/share/doc/icingaweb2/schema/pgsql.schema.sql
RUN rm -rf /run/httpd/* /tmp/httpd* && \
	rm -rf /etc/httpd/conf.d/README && \
	rm -rf /etc/httpd/conf.d/welcome.conf && \
	echo "<h1>Test Page<h1>" > /usr/share/httpd/noindex/index.html
RUN echo "ServerName 0.0.0.0" >> /etc/httpd/conf/httpd.conf
VOLUME ["/etc/icingaweb2"]
ENTRYPOINT ["/opt/rh/startup.sh"]
