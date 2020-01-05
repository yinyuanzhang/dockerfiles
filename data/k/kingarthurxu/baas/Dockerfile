FROM centos:7
MAINTAINER ArthurXu <arthur.xu@veritas.com>

ENV BAAS_VERSION=1.2

ADD ./requirements.txt /

RUN yum clean all \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && yum -y update \
    && yum install -y python-setuptools \
    && yum install -y gcc \
    && yum install -y python-devel \
    && easy_install pip \
    && pip install -r /requirements.txt \
        && yum clean all \
        && rm -rf /var/cache/yum \
        && rm -rf /root/.cache
