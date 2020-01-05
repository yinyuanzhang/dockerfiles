FROM debian:jessie-slim

RUN apt-get update
RUN apt-get install -y locales
RUN echo "Asia/Shanghai" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata && \
    echo "zh_CN.UTF-8 UTF-8" > /etc/locale.gen && \
    echo 'LANG="zh_CN.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=zh_CN.UTF-8

ENV JAVA_HOME     /usr/local/jre
ENV CATALINA_HOME /usr/local/tomcat

ADD jre-8u192-linux-x64.tar.gz   /tmp
ADD apache-tomcat-7.0.92.tar.gz  /tmp

RUN mv /tmp/jre1.8.0_192         $JAVA_HOME
RUN mv /tmp/apache-tomcat-7.0.92 $CATALINA_HOME
RUN rm -rf $CATALINA_HOME/webapps/*
RUN sed -i 's/connectionTimeout="20000"/connectionTimeout="20000"\ URIEncoding="UTF-8"/g' $CATALINA_HOME/conf/server.xml

ENV PATH $CATALINA_HOME/bin:$JAVA_HOME/bin:$PATH
ENV LANG zh_CN.UTF-8

WORKDIR $CATALINA_HOME

EXPOSE 8080
CMD ["catalina.sh", "run"]