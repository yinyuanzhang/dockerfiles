FROM htakeuchi/docker-asciidoctor-jp
LABEL MAINTAINER Hayato MIYAZAWA <mmsswrks@gmail.com>

ENV JAVA_HOME=/usr/lib/jvm/default-jvm \
    PATH=${PATH}:${JAVA_HOME}/bin:/fopub/bin

RUN apk add --no-cache \
    openjdk8 \
    && mkdir /fopub \
    && curl -L -s https://api.github.com/repos/asciidoctor/asciidoctor-fopub/tarball | tar xzf - -C /fopub/ --strip-components=1

WORKDIR /tmp

RUN touch empty.xml && fopub empty.xml && rm empty.xml

WORKDIR /documents
