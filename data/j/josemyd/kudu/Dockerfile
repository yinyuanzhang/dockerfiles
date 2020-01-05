FROM josemyd/centos-jdk:jdk-8

USER root

ADD cloudera-cdh5.repo /etc/yum.repos.d/
RUN rpm --import https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/RPM-GPG-KEY-cloudera \
    && yum install -y initscripts kudu kudu-master kudu-tserver kudu-client0 kudu-client-devel kudu-debuginfo \
    python-setuptools \
    && easy_install supervisor \
    && yum clean all

ADD etc/supervisord.conf /etc/
ADD etc/kudu/conf/tserver.gflagfile /etc/kudu/conf/

WORKDIR /

# Various helper scripts
ADD bin/start-kudu.sh /
ADD bin/supervisord-bootstrap.sh /
ADD bin/wait-for-it.sh /
RUN chmod +x ./*.sh

EXPOSE 8050 7050 8051 7051

#RUN chkconfig ntpd on

ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
