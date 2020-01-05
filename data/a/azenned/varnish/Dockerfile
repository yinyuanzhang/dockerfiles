FROM centos:centos6.8
MAINTAINER Przemyslaw Ozgo linux@ozgo.info, Marcin Ryzycki marcin@m12.io, ZENNED ABDERRAZAK azenned+github@gmail.com

RUN yum update -y && \
  yum install -y epel-release && \
  rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.1.el6.rpm && \
  yum install -y varnish && \
  yum install -y libmhash-devel && \
  yum clean all

ADD start.sh /start.sh

ENV VCL_CONFIG      /etc/varnish/default.vcl
ENV CACHE_SIZE      64m
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600

CMD /start.sh
EXPOSE 80
