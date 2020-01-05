# VERSION 1.1
# DOCKER-VERSION  1.2.0
# AUTHOR:         Richard Lee <lifuzu@gmail.com>
# DESCRIPTION:    Java7 Image Container

FROM dockerbase/ubuntu

# Run dockerbase script
ADD     java7.sh /dockerbase/
RUN     /dockerbase/java7.sh

ENV     JAVA_HOME /usr/local/java
ENV     JRE_HOME /usr/local/java/jre
ENV     PATH $PATH:$JAVA_HOME/bin:$JRE_HOME/bin
