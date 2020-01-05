FROM centos:latest as stage1

# build redis client library
RUN yum -y install gcc wget make && \
	wget https://github.com/redis/hiredis/archive/v0.13.3.tar.gz && \
	tar xzf v0.13.3.tar.gz && \
	cd hiredis-0.13.3 && \
	make && \
	make install

FROM centos:latest
COPY --from=stage1 /usr/local/ /usr/local/

RUN yum -y install postgresql-libs epel-release && \
  	yum -y install python-pip && \
    yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm && \
    yum install yum-utils && \
     yum-config-manager --enable remi-php73 && \
     yum update -y && \
  	yum -y install php73-php httpd php73-php-pgsql php73-php-xml && \
    yum -y install http://www.city-fan.org/ftp/contrib/yum-repo/city-fan.org-release-2-1.rhel7.noarch.rpm && \
    yum -y install --enablerepo=city-fan.org libcurl && \
  	pip install --upgrade pip && \
	  pip install supervisor && \
	  mkdir -p /var/lark /var/spool/lark /var/log/lark && \
	  echo /usr/local/lib >> /etc/ld.so.conf && \
	  ldconfig -v && \
	  sed -i -e 's/Listen 80/Listen 8000/' /etc/httpd/conf/httpd.conf

# larkd binaries
COPY larkd/ /var/lark/

#Kannel tree
COPY --chown=root:root kannel/bin/* /bin/
COPY --chown=root:root kannel/sbin/* /sbin/
COPY --chown=root:root kannel/lib/* /lib/
COPY --chown=root:root kannel/share/* /usr/share/
RUN /usr/sbin/ldconfig -v


#admin ui scipts
COPY admin/ /var/www/html/

RUN chown -R apache /var/www/html && \
	mkdir -p /var/spool/lark /var/log/lark && \
	chown -R apache /var/lark /var/spool/lark /var/log/lark /var/log/httpd

COPY entrypoint.sh /
COPY supervisord.conf /

ENV MBUNI_HOST larkd
ENV KANNEL_HOST kannel
ENV CONF_DIR /var/lark
ENV PGDATA /data
ENV POSTGRES_DB lark
ENV POSTGRES_USER lark
ENV POSTGRES_PASSWORD pg_pass
ENV POSTGRES_HOST postgres

CMD /usr/bin/supervisord -c /supervisord.conf

