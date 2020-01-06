FROM cloudpack/centos

RUN yum -y update
RUN yum -y install memcached
RUN yum -y clean all

RUN mkdir /var/log/memcached
RUN mkdir /var/run/memcached
RUN chown memcached.memcached /var/run/memcached

CMD /usr/bin/memcached -u memcached -s /var/run/memcached/memcached.sock >> /var/log/memcached/memcached.log 2>&1

VOLUME /var/run/memcached
VOLUME /var/log/memcached
