# Pull base image.
FROM sherylynn/wget
MAINTAINER Sherylynn <352281674@qq.com>

# install packages
RUN apk --update add --no-cache libffi-dev py-cffi
ENV XX_VERSION 3.12.10
ENV DOWNLOAD_URL https://codeload.github.com/XX-net/XX-Net/tar.gz/${XX_VERSION}
RUN wget -q --no-check-certificate ${DOWNLOAD_URL} && \
    tar -xzf ${XX_VERSION} && \
    mv XX-Net-${XX_VERSION} XX-Net && \
#    rm -rf /XX-Net/code/default/gae_proxy/server/ && \
#    rm -rf /XX-Net/code/default/python27/ && \
    rm ${XX_VERSION}
VOLUME ["/XX-Net/data"]
CMD ["python","/XX-Net/code/default/launcher/start.py"]
EXPOSE 8085 8086 8087
ENV LANG zh_CN.UTF-8
