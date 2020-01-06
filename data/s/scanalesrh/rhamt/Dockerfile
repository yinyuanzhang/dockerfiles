FROM openjdk:8
   
MAINTAINER scanales

ADD migrationtoolkit-rhamt-web-distribution-4.0.0.with-authentication.zip /tmp/migrationtoolkit-rhamt-web-distribution-4.0.0.with-authentication.zip
RUN unzip -o /tmp/migrationtoolkit-rhamt-web-distribution-4.0.0.with-authentication.zip -d /opt

EXPOSE 8080

ENTRYPOINT /opt/rhamt-web-distribution-4.0.0.Final/run_rhamt.sh
