FROM rijalati/alpine-zulu-jdk8:latest
MAINTAINER <ritchie@selectstar.com>


RUN apk --no-cache --update add bash \
&& cd /opt \
&& curl -Ls http://dl.bintray.com/sbt/native-packages/sbt/0.13.15/sbt-0.13.15.tgz \
| tar --strip-components=1 -xzvf -

ENTRYPOINT ["/opt/bin/sbt", "help"]
