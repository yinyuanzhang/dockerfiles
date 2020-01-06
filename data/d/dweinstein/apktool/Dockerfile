FROM seansummers/alpine-java:latest

WORKDIR /opt

RUN apk.static add curl

ADD https://github.com/dweinstein/analysis-runner/archive/master.zip /tmp/analysis-runner.zip
RUN unzip /tmp/analysis-runner.zip && \
    mv analysis-runner-master runner && \
    rm -f /tmp/runner.zip

ENV APKTOOL_VER apktool_2.0.0
WORKDIR /opt/apktool/
ADD https://bitbucket.org/iBotPeaches/apktool/downloads/${APKTOOL_VER}.jar /opt/apktool/apktool.jar

ADD ./unpack.sh /opt/apktool/unpack.sh

ENV APKTOOL /opt/apktool/apktool.jar

ENV JAVA java
ENV JAVA_OPTS -Xmx512M
ENV TOOL /opt/apktool/unpack.sh
ENV CONTENT_TYPE application/x-gzip
ENTRYPOINT ["/opt/runner/runner.sh", "${TOOL}"]

