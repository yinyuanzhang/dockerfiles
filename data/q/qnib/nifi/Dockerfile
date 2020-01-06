FROM qnib/alpn-jdk8

ARG NIFI_VER=0.7.0
EXPOSE 8080

RUN wget -qO- http://mirrors.advancedhosters.com/apache/nifi/${NIFI_VER}/nifi-${NIFI_VER}-bin.tar.gz |tar -xzf -  -C /opt/ \
 && mv /opt/nifi-${NIFI_VER} /opt/nifi/
ADD opt/qnib/nifi/bin/start.sh /opt/qnib/nifi/bin/
ADD etc/supervisord.d/nifi.ini /etc/supervisord.d/
ADD etc/consul.d/nifi.json /etc/consul.d/
