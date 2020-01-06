FROM openshift/base-centos7

RUN yum install openssl-libs ImageMagick -y \
  && localedef -i en_US -f UTF-8 en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_ALL en_US.UTF-8

USER 1001
