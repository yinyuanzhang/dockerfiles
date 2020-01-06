FROM openjdk:8-slim

ENV MAVEN_HOME /opt/maven
ENV TZ Europe/Rome
ENV PATH $MAVEN_HOME/bin:$PATH

COPY cacerts $JAVA_HOME/jre/lib/security/
COPY 01-cert-ISP.crt /usr/local/share/ca-certificates/

RUN apt-get update && \
    apt-get install -y --no-install-recommends ssh wget tzdata doxygen python python-pip python-setuptools && \
    pip install wheel python-docx && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    wget -O maven.tar.gz http://apache.panu.it/maven/maven-3/3.5.4/binaries/apache-maven-3.5.4-bin.tar.gz  && \
    mkdir -p ${MAVEN_HOME} && tar zxf maven.tar.gz --strip-components=1 -C ${MAVEN_HOME} && \
    rm -f maven.tar.gz
