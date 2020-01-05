FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y tzdata \
    && apt-get install -y maven \
    && rm -rf /var/lib/apt/lists/*

RUN echo "Asia/Shanghai" > /etc/timezone \
    && ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

ADD ./jdk1.8.0_112.tar.gz /opt

RUN ln -s /opt/jdk1.8.0_112 /opt/j2sdk
ENV PATH="/opt/j2sdk/bin:${PATH}"

