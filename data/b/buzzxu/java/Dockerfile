FROM azul/zulu-openjdk-debian:13 AS jlink

# jdir=$(dirname $(dirname $(find / -name javac)))
RUN jdir=$(dirname $(dirname $(find /usr/lib/jvm -name javac))) && \
    jlink --compress=2  --no-man-pages --no-header-files --module-path ${jdir}/jmods  --add-modules java.base,java.desktop,java.instrument,java.logging,java.management,java.net.http,java.naming,java.rmi,java.security.jgss,java.sql,java.sql.rowset,java.xml,jdk.unsupported --bind-services --output /jre


FROM debian:buster-slim    

LABEL MAINTAINER buzzxu <downloadxu@163.com>

RUN rm -rf /var/lib/apt/lists/* && \  
    apt-get clean && \
    apt-get update -qq && \ 
    apt-get upgrade -y && \
    apt-get install -qq -y --no-install-recommends openssl libfontconfig1 && \
    rm /etc/localtime && \
    ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \ 
    echo "Asia/Shanghai" > /etc/timezone && \
    mkdir -p /opt/jre && \
    chmod a+x /opt/jre && \
    ln -svT /opt/jre /java-home && \
    apt-get autoclean && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* 

COPY --from=jlink /jre /opt/jre/ 

    
ENV TZ Asia/Shanghai
ENV LANG C.UTF-8
ENV JAVA_HOME /java-home
ENV JAVA_VERSION 13
ENV PATH $PATH:$JAVA_HOME/bin
CMD ["jshell"]

