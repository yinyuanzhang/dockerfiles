FROM adoptopenjdk/openjdk8:alpine-slim

LABEL de.kdac.tomcat.maintainer = "Claus Böhmer" \
      de.kdac.tomcat.authors = "eso@bistum-eichstaett.de" \
      de.kdac.tomcat.url = "https://hub.docker.com/r/kidac/tomcat" \
      de.kdac.tomcat.documentation = "https://hub.docker.com/r/kidac/tomcat" \
      de.kdac.tomcat.source = "https://github.com/kidac/tomcat" \
      de.kdac.tomcat.version = "8.5" \ 
      de.kdac.tomcat.vendor = "KDAC - https://ews.kdac.de" \
      de.kdac.tomcat.licenses = "http://www.apache.org/licenses/" \
      de.kdac.tomcat.title = "Tomcat (KDAC Version)" \
      de.kdac.tomcat.description = "Adapted Tomcat Dockerfile used by KDAC"

ENV TOMCAT_MAJOR=8
ENV TOMCAT_VERSION=8.5.45
ENV CATALINA_HOME=/opt/tomcat

RUN apk upgrade --update --no-cache
RUN apk add curl ttf-dejavu tini

RUN mkdir -p /opt

RUN curl -jkSL -o /tmp/apache-tomcat.tar.gz http://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz \
 && gunzip /tmp/apache-tomcat.tar.gz \
 && tar -C /opt -xf /tmp/apache-tomcat.tar \
 && ln -s /opt/apache-tomcat-$TOMCAT_VERSION $CATALINA_HOME \
 && rm -rf /tmp/apache-tomcat*

EXPOSE 8080

COPY entrypoint.sh              /entrypoint.sh

ENTRYPOINT /entrypoint.sh

WORKDIR $CATALINA_HOME
