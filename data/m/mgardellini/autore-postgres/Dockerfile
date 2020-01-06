FROM centos:centos6
MAINTAINER Mariano Gardellini <mariano.gardellini@gmail.com>

RUN yum localinstall -y http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-centos93-9.3-1.noarch.rpm
RUN yum install -y yum install postgresql93-server

ADD ./run.sh /usr/local/bin/run
RUN chmod +x /usr/local/bin/run

EXPOSE 5432

ENTRYPOINT ["/usr/local/bin/run"]
