FROM debian:jessie-slim

RUN apt-get update
RUN apt-get install -y locales
RUN echo "Asia/Chongqing" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    echo "zh_CN.UTF-8 UTF-8" > /etc/locale.gen && \
    echo 'LANG="zh_CN.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=zh_CN.UTF-8

ENV JAVA_HOME     /usr/local/jre

ADD jre-8u192-linux-x64.tar.gz   /tmp
RUN mv /tmp/jre1.8.0_192         $JAVA_HOME
ENV PATH $JAVA_HOME/bin:$PATH
ENV LANG zh_CN.UTF-8

VOLUME /vol/development

RUN mkdir -p /vol/development

EXPOSE 8086

WORKDIR /vol/development
