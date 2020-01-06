## Custom Dockerfile
FROM consol/sakuli-centos-xfce

MAINTAINER c-kr
ENV REFRESHED_AT 2018-02-13
ENV TZ=Europe/Berlin

## Install RDP
USER 0
RUN yum update -y; yum clean all
RUN yum install -y freerdp.x86_64 freerdp-libs.x86_64 freerdp-plugins.x86_64; yum clean all

## switch back to default user
USER 1984
