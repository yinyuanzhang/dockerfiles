FROM centos:centos7

MAINTAINER Ontheway <1057956918@qq.com>

COPY --chown=root:root Nessus-8.4.0-es7.x86_64.rpm /

RUN yum update -y \
    && rpm -ivh /Nessus-8.4.0-es7.x86_64.rpm \
    && rm -rf /Nessus-8.4.0-es7.x86_64.rpm

EXPOSE 8834

CMD /opt/nessus/sbin/nessusd
