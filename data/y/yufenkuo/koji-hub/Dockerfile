FROM centos:centos7

RUN yum -y update && \
    yum -y install \
           epel-release \
           git \
           gcc \
           yum-utils \
           tar \
           bzip2 \
           rpm-build \
           make \
           httpd \
           mod_ssl \
           python-devel \
           postgresql-server \
           mod_wsgi \
           koji \
           koji-hub \
           mod_python \
           koji-web \
           sudo \
           openssh-server \
           wget 

RUN yum clean all
RUN /usr/bin/ssh-keygen -A

EXPOSE 22 80 443
ADD etc/ /etc/
ADD root/ /root/
RUN chmod 600 /root/.pgpass
ADD bin/ /usr/local/bin
RUN chmod +x /usr/local/bin/*
ENV KOJI_OUTPUT /srv
ENV COMMON_CONFIG /config
ENV DO_INSTALLATION true

RUN mkdir -p ${KOJI_OUTPUT}/koji/{packages,repos,work,scratch,repos-dist}
RUN chown apache.apache ${KOJI_OUTPUT}/koji/*

ENTRYPOINT /usr/local/bin/entrypoint.sh

