FROM openjdk:8-jdk-alpine
MAINTAINER xuxueli

ENV PARAMS=""

ENV TZ=PRC
RUN apk update && apk upgrade && apk add netcat-openbsd
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD target/batch-admin-*.jar /app.jar

ENTRYPOINT ["sh","-c","java -jar /app.jar $PARAMS"]