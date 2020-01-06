FROM openjdk:jre-alpine
LABEL maintainer "Niko Virtala <niko@nikovirtala.io>"

RUN apk add --no-cache --virtual curl ca-certificates grep && \
  _bfgversion=$(curl -s http://repo1.maven.org/maven2/com/madgag/bfg/maven-metadata.xml | grep release | grep -oE '\d+.\d+.\d+') && \
  curl -sSLO http://repo1.maven.org/maven2/com/madgag/bfg/${_bfgversion}/bfg-${_bfgversion}.jar && \
  mv bfg-${_bfgversion}.jar /usr/local/bin/bfg.jar

RUN adduser -D -g '' -h /home/nikovirtala nikovirtala
USER nikovirtala
WORKDIR /home/nikovirtala

ENTRYPOINT ["java", "-jar", "/usr/local/bin/bfg.jar"]
