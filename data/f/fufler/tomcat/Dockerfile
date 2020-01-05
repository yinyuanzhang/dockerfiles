FROM tomcat:7-jre8
MAINTAINER Alexey Ermakov <fufler@gmail.com>


# ENV http_proxy=http://proxy:3128/

RUN apt-get update -qq && apt-get install -qq python3 && apt-get -qq clean

COPY bin  /usr/local/tomcat/bin/
COPY conf /usr/local/tomcat/conf
COPY keystore /usr/local/tomcat/keystore/

VOLUME /usr/local/tomcat/logs

CMD run.py

EXPOSE 8080 8443
