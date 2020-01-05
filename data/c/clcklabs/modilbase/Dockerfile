####
#
#  We use openJDK/JRE because of licencing problems when using containers for redistribution of Oracle Java
#  ref: https://blog.takipi.com/running-java-on-docker-youre-breaking-the-law/
#
#  Martin Hermosilla - 2018
#
###

FROM openjdk:13-jdk-alpine

MAINTAINER Martin Hermosilla <martin.hermosilla@artibonitech.com>

RUN apk add --no-cache curl python

ADD scripts/waitfor.sh /bin/waitfor
RUN chmod +x /bin/waitfor

COPY scripts/entrypoint.py /bin/entrypoint
RUN chmod +x /bin/entrypoint
