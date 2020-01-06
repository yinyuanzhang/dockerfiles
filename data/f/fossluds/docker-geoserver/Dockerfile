FROM tomcat:8-jre8

MAINTAINER Ludger FOSS <fossluds@t-online.de>

ENV GEOSERVER_VERSION 2.13.1
ENV GEOSERVER_DATA_DIR /var/local/geoserver
ENV GEOSERVER_INSTALL_DIR /usr/local/geoserver
ENV GEOSERVER_EXTENSION_SUFFIX_INSTALL_DIR WEB-INF/lib

# Uncomment to use APT cache (requires apt-cacher-ng on host)
#RUN echo "Acquire::http { Proxy \"http://`/sbin/ip route|awk '/default/ { print $3 }'`:3142\"; };" > /etc/apt/apt.conf.d/71-apt-cacher-ng

# Microsoft fonts
RUN echo "deb http://httpredir.debian.org/debian jessie contrib" >> /etc/apt/sources.list
RUN set -x \
	&& apt-get update \
	&& apt-get install -yq ttf-mscorefonts-installer \
	&& rm -rf /var/lib/apt/lists/*

# Native JAI & ImageIO
RUN cd /usr/lib/jvm/java-8-openjdk-amd64 \
	&& wget http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-amd64-jdk.bin \
	&& tail -n +139 jai-1_1_3-lib-linux-amd64-jdk.bin > INSTALL-jai \
	&& chmod u+x INSTALL-jai \
	&& ./INSTALL-jai \
	&& rm jai-1_1_3-lib-linux-amd64-jdk.bin INSTALL-jai *.txt \
	&& wget http://download.java.net/media/jai-imageio/builds/release/1.1/jai_imageio-1_1-lib-linux-amd64-jdk.bin \
	&& tail -n +215 jai_imageio-1_1-lib-linux-amd64-jdk.bin > INSTALL-jai_imageio \
	&& chmod u+x INSTALL-jai_imageio \
	&& ./INSTALL-jai_imageio \
	&& rm jai_imageio-1_1-lib-linux-amd64-jdk.bin INSTALL-jai_imageio *.txt

# GeoServer
ADD conf/geoserver.xml /usr/local/tomcat/conf/Catalina/localhost/geoserver.xml
RUN mkdir ${GEOSERVER_DATA_DIR} \
	&& mkdir ${GEOSERVER_INSTALL_DIR} \
	&& cd ${GEOSERVER_INSTALL_DIR} \
	&& wget http://sourceforge.net/projects/geoserver/files/GeoServer/${GEOSERVER_VERSION}/geoserver-${GEOSERVER_VERSION}-war.zip \
	&& unzip geoserver-${GEOSERVER_VERSION}-war.zip \
	&& unzip geoserver.war \
	&& mv data/* ${GEOSERVER_DATA_DIR} \
	&& rm -rf geoserver-${GEOSERVER_VERSION}-war.zip geoserver.war target *.txt

# GeoServer Extensions
RUN mkdir -p ${GEOSERVER_DATA_DIR}/tempExt

ADD getExtensions.sh ${GEOSERVER_DATA_DIR}/tempExt/getExtensions.sh
ADD extensions ${GEOSERVER_DATA_DIR}/tempExt/extensions

RUN chmod +x ${GEOSERVER_DATA_DIR}/tempExt/getExtensions.sh \
#RUN ["executable", "param1", "param2"] (exec form)
#RUN ["/var/local/geoserver/tempExt/getExtensions.sh", "-v", "2.13.1", "-t", "."]
	&& cd ${GEOSERVER_DATA_DIR}/tempExt \
	# && echo "myDebug" \
	# && pwd \
	# && ls -l \
	# && id \
	# && groups \
	# && which bash \
	# && which sh \
	&& /bin/sh /var/local/geoserver/tempExt/getExtensions.sh \
	&& cp ${GEOSERVER_DATA_DIR}/tempExt/*.jar ${GEOSERVER_INSTALL_DIR}/${GEOSERVER_EXTENSION_SUFFIX_INSTALL_DIR} \
	&& cd ${GEOSERVER_DATA_DIR} \
	&& rm -rf ${GEOSERVER_DATA_DIR}/tempExt

# for debugging
##RUN ls -l && pwd


# Enable CORS
RUN sed -i '\:</web-app>:i\
    <filter>\
        <filter-name>CorsFilter</filter-name>\
        <filter-class>org.apache.catalina.filters.CorsFilter</filter-class>\
    </filter>\
\
    <filter-mapping>\
        <filter-name>CorsFilter</filter-name>\
        <url-pattern>/*</url-pattern>\
    </filter-mapping>\
\
    <init-param>\
        <param-name>cors.support.credentials</param-name>\
        <param-value>true</param-value>\
    </init-param>' ${GEOSERVER_INSTALL_DIR}/WEB-INF/web.xml

# Tomcat environment
ENV CATALINA_OPTS "-server -Djava.awt.headless=true \
	-Xms768m -Xmx1560m -XX:+UseConcMarkSweepGC -XX:NewSize=48m \
	-DGEOSERVER_DATA_DIR=${GEOSERVER_DATA_DIR}"

ADD start.sh /usr/local/bin/start.sh
CMD start.sh

EXPOSE 8080
