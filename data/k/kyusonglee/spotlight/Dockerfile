FROM openjdk:8-jre-alpine

MAINTAINER  Kyusong Lee <kyusongl@convmind.ai>

ENV RELEASE_SERVER    convmind-models.s3.us-east-2.amazonaws.com/basic-models
ENV RELEASE_FILENAME  dbpedia-spotlight-1.0.0.jar 
ENV LANGUAGE_MODEL    en.tar

RUN apk add --no-cache curl && \
    mkdir -p /opt/spotlight && \
    cd /opt/spotlight && \
    curl -O "http://$RELEASE_SERVER/$RELEASE_FILENAME" && \
    curl -O "http://$RELEASE_SERVER/$LANGUAGE_MODEL" && \
    tar xvf $LANGUAGE_MODEL  && \
    rm  $LANGUAGE_MODEL && \
    apk del curl


ADD spotlight.sh /bin/spotlight.sh
RUN chmod +x /bin/spotlight.sh

EXPOSE 2222
