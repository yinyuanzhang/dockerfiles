FROM ubuntu:18.04
MAINTAINER Wang, Tao <i@miffyliye.org>

ARG VERSION=0.27.0
ENV FILENAME frp_${VERSION}_linux_amd64.tar.gz
ENV DOWNLOAD_URL https://github.com/fatedier/frp/releases/download/v${VERSION}/frp_${VERSION}_linux_amd64.tar.gz

RUN apt-get update \
    && apt-get install -y wget tar \
    && wget ${DOWNLOAD_URL} \
    && tar xzf ${FILENAME} \
    && mkdir /root/frp \
    && mv /frp_${VERSION}_linux_amd64/* /root/frp \
    && rm -rf /frp_${VERSION}_linux_amd64/ \
    && rm -rf /${FILENAME}

ADD ./docker_entrypoint.sh /usr/local/bin/docker_entrypoint.sh
RUN chmod a+x /usr/local/bin/docker_entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker_entrypoint.sh"]