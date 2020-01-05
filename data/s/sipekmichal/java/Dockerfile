FROM debian:jessie

LABEL maintainer="mich.sipek@gmail.com"

ADD https://d3pxv6yz143wms.cloudfront.net/java-1.8.0-amazon-corretto-jdk_8.192.12-2_amd64.deb ./
COPY local_policy.jar US_export_policy.jar /opt/

RUN echo "CET" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata && \    
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install vim dnsutils telnet software-properties-common redis-tools wget libfontconfig1 -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes java-common && \
    dpkg --install java-1.8.0-amazon-corretto-jdk_8.192.12-2_amd64.deb  && \
    rm -rf java-1.8.0-amazon-corretto-jdk_8.192.12-2_amd64.deb && \
    apt-get clean all && \
    rm -rf /var/lib/apt/lists/* && \
    mv /opt/*.jar /usr/lib/jvm/java-1.8.0-amazon-corretto/jre/lib/security/

VOLUME /etc/timezone:/etc/localtime

ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-amazon-corretto

CMD ["/bin/bash"]
