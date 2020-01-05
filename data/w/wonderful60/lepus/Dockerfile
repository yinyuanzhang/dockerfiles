FROM centos:6.6

#ENV LEPUS_VERSION Lepus_v3.8_beta

RUN \
yum install -y httpd php php-mysql gcc libffi-devel python-devel openssl-devel mysql-server mysql mysql-devel net-snmp* && \
yum clean all && rm -rf /var/lib/mysql

COPY lepus /lepus

RUN \
cd /lepus/MySQLdb1-master/ && \
python setup.py build && python setup.py install && \
cd /lepus/pymongo-3.7.2/ && python setup.py install && \
cd /lepus/redis-2.10.6/ && python setup.py install

RUN \
cd /lepus/ && \
chmod +x /lepus/Lepus_v3.8_beta/python/install.sh && \
chmod +x /lepus/run.sh && \
cd /lepus/Lepus_v3.8_beta/python/ && bash install.sh

RUN cp -r /lepus/Lepus_v3.8_beta/php/* /var/www/html/

RUN chmod +x /lepus/config.sh && sh /lepus/config.sh

CMD ["/lepus/run.sh"]
