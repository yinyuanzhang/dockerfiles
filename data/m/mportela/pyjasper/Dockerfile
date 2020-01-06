# pyJasper
#
# VERSION               6.0.0

FROM      mportela/oracle-java7:latest

MAINTAINER Marcel Portela <marcel.portela@gmail.com>

ADD ./ /usr/local/pyJasper

EXPOSE 5555

ENTRYPOINT /usr/local/pyJasper/pyjasper/backend/pyJasper-httpd.sh -Xms128m -Xmx512m
