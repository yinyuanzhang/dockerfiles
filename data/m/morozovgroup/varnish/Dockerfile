FROM centos:7

ADD varnishcache_varnish60.repo /etc/yum.repos.d/varnishcache_varnish60.repo

RUN yum update -y && \
  yum install pygpgme yum-utils && \
  yum install -y epel-release && \
  yum install -y varnish && \
  yum install -y libmhash-devel && \
  yum clean all

ADD start.sh /start.sh

ENV VCL_CONFIG      /etc/varnish/default.vcl
ENV CACHE_SIZE      64m
ENV VARNISHD_PARAMS -a :8080 -p default_ttl=3600 -p default_grace=3600

CMD /start.sh

RUN usermod -a -G root varnish && chmod g+rwx /var/lib/varnish
USER varnish

EXPOSE 8080
