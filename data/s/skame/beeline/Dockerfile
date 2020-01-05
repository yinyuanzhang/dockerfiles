FROM openjdk:8-jre

MAINTAINER Satoshi KAMEI "skame@nttv6.jp"

#BEEEEEEEELINE
RUN curl http://package.mapr.com/releases/pub/maprgpg.key | apt-key add -
RUN echo "deb http://package.mapr.com/releases/v5.2.0/ubuntu/ mapr optional" >> /etc/apt/sources.list
RUN echo "deb http://package.mapr.com/releases/ecosystem-5.x/ubuntu binary/" >> /etc/apt/sources.list
RUN apt-get update && apt install -y --no-install-recommends --allow-unauthenticated mapr-hive && \
        apt-get clean && rm -rf /var/lib/apt/lists/*
RUN ln -s /opt/mapr/hive/hive-1.2/bin/beeline /usr/bin/beeline

CMD ["/bin/bash"]
