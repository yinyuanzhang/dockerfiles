FROM centos:7
RUN yum install -y squid
COPY squid.conf /etc/squid/squid.conf
# Elite proxy set
RUN echo 'request_header_access Via deny all' >> /etc/squid/squid.conf \
 && echo 'request_header_access X-Forwarded-For deny all' >> /etc/squid/squid.conf \
 && echo 'request_header_access From deny all' >> /etc/squid/squid.conf \
# &&  sed -i 's/http_access deny all/http_access allow all/g' /etc/squid/squid.conf \
# && sed -i 's/http_port 3128/http_port 57112/g' /etc/squid/squid.conf
ENTRYPOINT /usr/sbin/squid start && /bin/bash
EXPOSE 57112
