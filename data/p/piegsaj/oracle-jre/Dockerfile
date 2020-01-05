FROM          ubuntu:18.04
MAINTAINER    Jens Piegsa <piegsa@gmail.com>

ENV VERSION   8
ENV UPDATE    172
ENV BUILD     11
ENV URL_HASH  a58eab1ec242421181065cdc37240b08

ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle
ENV JRE_HOME  ${JAVA_HOME}/jre
ENV PATH      ${JAVA_HOME}/bin:${PATH}

RUN apt-get update && \
    apt-get install ca-certificates curl -y && \
    curl --silent --location --retry 3 --cacert /etc/ssl/certs/GeoTrust_Global_CA.pem \
         --header "Cookie: oraclelicense=accept-securebackup-cookie;" \
         http://download.oracle.com/otn-pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/"${URL_HASH}"/server-jre-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz \
         | tar xz -C /tmp && \
    mkdir -p /usr/lib/jvm && \
    mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" && \
    apt-get autoclean && \
    apt-get --purge -y autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN update-alternatives --install "/usr/bin/java" "java" "${JRE_HOME}/bin/java" 1 && \
    update-alternatives --install "/usr/bin/javac" "javac" "${JAVA_HOME}/bin/javac" 1 && \
    update-alternatives --set java "${JRE_HOME}/bin/java" && \
    update-alternatives --set javac "${JAVA_HOME}/bin/javac"
