FROM centos:7.6.1810

ENV VERSION 6-4-4

MAINTAINER Cort Eyer
# Forked from BibCNRS <bibcnrs@inist.fr>

RUN yum -y update \
  && yum -y install curl lib32z1 dnsutils vim

WORKDIR /usr/local/ezproxy
COPY docker-entrypoint.sh /entrypoint.sh

RUN curl -sS -k https://www.oclc.org/content/dam/support/ezproxy/documentation/download/binaries/$VERSION/ezproxy-linux.bin > ./ezproxy \
&& chmod 755 ./ezproxy

EXPOSE 80
EXPOSE 443

ENTRYPOINT ["/entrypoint.sh"]
