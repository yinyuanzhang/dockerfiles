FROM ubuntu:latest
MAINTAINER zopanix <zopanix@gmail.com>
ENV CASPERJS_VERSION=1.1.4-1
#see: https://github.com/moby/moby/issues/5539
ENV QT_QPA_PLATFORM=offscreen
ADD ./resources /resources
RUN /resources/build && rm -rf resources
ENTRYPOINT ["casperjs"]
VOLUME /data
WORKDIR /data
