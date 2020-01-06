from docker:latest

RUN apk add --no-cache bash git openjdk8 java-cacerts curl openssh

ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
RUN ln -s $JAVA_HOME/bin/javac /usr/bin/javac

ENTRYPOINT sh

