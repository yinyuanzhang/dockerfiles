FROM openjdk:8-jre

LABEL maintainer "luhuiguo@gmail.com"

RUN wget "http://dl.mycat.io/1.6-RELEASE/Mycat-server-1.6-RELEASE-20161028204710-linux.tar.gz" -P /opt

RUN tar zxvf /opt/Mycat-server-1.6-RELEASE-20161028204710-linux.tar.gz -C /opt

EXPOSE 8066
VOLUME ["/opt/mycat/conf"]

ENV MYCAT_HOME=/opt/mycat
ENV PATH=$PATH:$MYCAT_HOME/bin

ENTRYPOINT ["/opt/mycat/bin/mycat", "console"]
