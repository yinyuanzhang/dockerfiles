# sepage/play215_github
#
# VERSION               0.0.1

FROM debian:wheezy
MAINTAINER Fred CECILIA <fred@sepage.fr>

ENV PLAY_VERSION 2.1.5
ENV PATH $PATH:/opt/play-$PLAY_VERSION
ENV SSH_PRIVATE ./id_rsa
ENV SSH_PUB ./id_rsa.pub
ENV SSH_DIR /root/.ssh


#INSTALL 
RUN apt-get update && apt-get install -y openjdk-7-jdk unzip ssh git

#PLAY
ADD http://downloads.typesafe.com/play/$PLAY_VERSION/play-$PLAY_VERSION.zip /tmp/play-$PLAY_VERSION.zip
RUN (cd /opt && unzip /tmp/play-$PLAY_VERSION.zip && rm -f /tmp/play-$PLAY_VERSION.zip)


#SSH
RUN mkdir $SSH_DIR 
RUN ssh-keyscan -H github.com >> $SSH_DIR/known_hosts 

ONBUILD COPY $SSH_PRIVATE $SSH_DIR/id_rsa
ONBUILD COPY $SSH_PUB $SSH_DIR/id_rsa.pub
ONBUILD RUN chmod 600 $SSH_DIR/id_rsa
ONBUILD RUN chmod 600 $SSH_DIR/id_rsa.pub


EXPOSE 9000

