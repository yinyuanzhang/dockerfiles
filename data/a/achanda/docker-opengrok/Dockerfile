FROM debian:sid
MAINTAINER Abhishek Chanda

ENV OPENGROK_INSTANCE_BASE /grok

RUN apt-get update
RUN apt-get install -y openjdk-7-jre-headless exuberant-ctags git subversion mercurial tomcat6 wget inotify-tools
ADD install.sh /usr/local/bin/install
RUN /usr/local/bin/install
ADD run.sh /usr/local/bin/run
ENTRYPOINT ["/usr/local/bin/run"]

EXPOSE 8080
EXPOSE 22
