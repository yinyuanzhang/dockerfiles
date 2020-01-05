# Sphinx Search

FROM centos:7

MAINTAINER PazitiFF

RUN yum install -y postgresql-libs unixODBC \
    && yum install -y wget mc glibc mariadb-libs \
    && yum -y install mysql \
    && cd /tmp \
    && wget http://sphinxsearch.com/files/sphinx-2.2.11-1.rhel7.x86_64.rpm \
    && yum install -y sphinx-2.2.11-1.rhel7.x86_64.rpm \
    && rm sphinx-2.2.11-1.rhel7.x86_64.rpm \
    && mkdir /etc/sphinx/dicts

COPY dicts/ru.pak /etc/sphinx/dicts/ru.pak
#COPY sphinx.conf /etc/sphinx/sphinx.conf

# expose ports
EXPOSE 9312 9306

# prepare directories
RUN mkdir -p /var/idx/sphinx && \
    mkdir -p /var/log/sphinx && \
    mkdir -p /var/lib/sphinx && \
    mkdir -p /var/run/sphinx && \
    mkdir -p /var/diz/sphinx

# dicts
ADD dicts /var/diz/sphinx

# Expose some folders for configurations
VOLUME ["/var/idx/sphinx", "/var/log/sphinx", "/var/lib/sphinx", "/var/run/sphinx", "/var/diz/sphinx"]

ADD indexall.sh /
RUN chmod a+x indexall.sh

# scripts
ADD searchd.sh /
RUN chmod a+x searchd.sh
RUN /searchd.sh

# run the script
#CMD ["./indexall.sh"]
#CMD /usr/bin/searchd && tail /var/log/sphinx/searchd.log
#CMD /usr/bin/searchd && tail /etc/sphinx/sphinx.conf
#CMD /usr/bin/searchd