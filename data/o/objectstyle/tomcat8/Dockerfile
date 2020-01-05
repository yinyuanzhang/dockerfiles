FROM objectstyle/java8:latest

MAINTAINER Andrus Adamchik <andrus at objectstyle dot com>

LABEL name=objectstyle-tomcat8

RUN yum -y install tar
RUN yum -y update; yum clean all

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# see https://www.apache.org/dist/tomcat/tomcat-8/KEYS
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys \
	05AB33110949707C93A279E3D3EFE6B686867BA6 \
	07E48665A34DCAFAE522E5E6266191C37C037D42 \
	47309207D818FFD8DCD3F83F1931D684307A10A5 \
	541FBE7D8F78B25E055DDEE13C370389288584E7 \
	61B832AC2F1C5A90F0F9B00A1C506407564C17A3 \
	79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED \
	9BA44C2621385CB966EBA586F72C284D731FABEE \
	A27677289986DB50844682F8ACB77FC2E86E29AC \
	A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 \
	DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 \
	F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE \
	F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23

ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.0.32
ENV TOMCAT_TGZ_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz

ENV MYSQL_CONNECTOR_VERSION 5.1.35
ENV MYSQL_DRIVER_URL https://repo1.maven.org/maven2/mysql/mysql-connector-java/$MYSQL_CONNECTOR_VERSION/mysql-connector-java-$MYSQL_CONNECTOR_VERSION.jar

ENV JAVAMAIL_VERSION 1.4.7
ENV JAVAMAIL_URL https://repo1.maven.org/maven2/javax/mail/mail/$JAVAMAIL_VERSION/mail-$JAVAMAIL_VERSION.jar

RUN set -x \
	&& curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz \
	&& curl -fSL "$TOMCAT_TGZ_URL.asc" -o tomcat.tar.gz.asc \
	&& gpg --verify tomcat.tar.gz.asc \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm -rf webapps/* \
	&& rm tomcat.tar.gz* \
	&& yum -y remove tar \
	&& curl -fSL "$MYSQL_DRIVER_URL" -o lib/mysql-connector-java-$MYSQL_CONNECTOR_VERSION.jar \
	&& curl -fSL "$JAVAMAIL_URL" -o lib/mail-$JAVAMAIL_VERSION.jar

ADD docker-startup.sh bin/docker-startup.sh

ENTRYPOINT ["docker-startup.sh"]
