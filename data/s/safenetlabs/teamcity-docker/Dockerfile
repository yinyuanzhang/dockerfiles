FROM java:8

MAINTAINER Sjoerd Mulder <sjoerd@crobox.com>

ENV TEAMCITY_VERSION 2018.2.2

ENV TEAMCITY_DATA_PATH /var/lib/teamcity

# Get and install teamcity
RUN wget -qO- https://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.tar.gz | tar xz -C /opt

# Enable the correct Valve when running behind a proxy
RUN sed -i -e "s/\.*<\/Host>.*$/<Valve className=\"org.apache.catalina.valves.RemoteIpValve\" remoteIpHeader=\"x-forwarded-for\" protocolHeader=\"x-forwarded-proto\" portHeader=\"x-forwarded-port\" \/><\/Host>/" /opt/TeamCity/conf/server.xml

COPY docker-entrypoint.sh /docker-entrypoint.sh

COPY gemalto2017root.pem /tmp
RUN keytool -importcert -noprompt -alias gemaltoroot -keystore /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/cacerts -file /tmp/gemalto2017root.pem -storepass changeit

COPY blackduckhubl1-emea.gemalto.com.crt /tmp
RUN keytool -importcert -noprompt -alias bdroot -keystore /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/cacerts -file /tmp/blackduckhubl1-emea.gemalto.com.crt -storepass changeit

EXPOSE  8111

VOLUME /var/lib/teamcity

ENTRYPOINT ["/docker-entrypoint.sh"]
