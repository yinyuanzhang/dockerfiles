FROM centos:7
MAINTAINER Apriorit

USER root

RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && yum -y update && yum -y install deltarpm \
libmcrypt-devel python35u python35u-pip python35u-devel gcc mysql-devel && yum clean all && rm -rf /var/cache/yum

RUN localedef -i en_US -f UTF-8 en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY mcrypt /mcrypt
WORKDIR /mcrypt
RUN python3.5 setup.py install

COPY --from=apriorit/docker-centos7-x64-python35-gcc:latest \
["/lib64/libc++.so.1", "/lib64/libc++abi.so.1", "/lib64/libicudata.so.56", "/lib64/libicui18n.so.56", \
"/lib64/libicuuc.so.56", "/lib64/libQt5Core.la", "/lib64/libQt5Core.so.5", "/lib64/"]

RUN pip3.5 install boto3==1.4.2 botocore==1.8.26 billiard==3.5.0.3 configparser==3.5.0 Django==1.10.4 \
djangorestframework==3.5.3 celery==4.0.2 mysqlclient==1.3.9 pprp==0.2.5 pycrypto==2.6.1 pynamodb==2.0.3 \
requests==2.12.4 s3transfer==0.1.10 sendgrid==3.6.3 spyne==2.12.14 wrapt==1.10.8 gunicorn==19.6.0 aiohttp==0.21.6 \
pysftp==0.2.9 suds-py3==1.3.3.0 lxml==3.7.3 flower==0.9.1 amqp==2.1.4 validate-email==1.3