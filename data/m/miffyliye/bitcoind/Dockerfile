FROM ubuntu:18.04
MAINTAINER Wang, Tao <i@miffyliye.org>

ARG VERSION=0.16.3

ENV FILENAME bitcoin-${VERSION}-x86_64-linux-gnu.tar.gz
ENV DOWNLOAD_URL https://bitcoin.org/bin/bitcoin-core-${VERSION}/${FILENAME}

RUN apt-get update \
  && apt-get install -y wget tar \
  && wget ${DOWNLOAD_URL} \
  && tar xzf ${FILENAME} \
  && mkdir /root/.bitcoin \
  && mv /bitcoin-${VERSION}/bin/* /usr/local/bin/ \
  && rm -rf /bitcoin-${VERSION}/ \
  && rm -rf /${FILENAME}

ADD ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh
RUN chmod a+x /usr/local/bin/docker_entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker_entrypoint.sh"]
