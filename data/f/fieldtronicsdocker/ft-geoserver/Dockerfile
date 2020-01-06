# docker file modified from https://hub.docker.com/r/kartoza/geoserver/~/dockerfile/ #
#--------- Generic stuff all our Dockerfiles should start with so we get caching ------------
FROM tomcat:8.0-jre8

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl
#RUN  ln -s /bin/true /sbin/initctl

RUN apt-get -y update

#Install extra fonts to use with sld font markers
RUN apt-get install -y  fonts-cantarell lmodern ttf-aenigma ttf-georgewilliams ttf-bitstream-vera ttf-sjfonts tv-fonts \
    build-essential libapr1-dev libssl-dev default-jdk
#-------------Application Specific Stuff ----------------------------------------------------

ARG GS_VERSION=2.13.0
ARG GS_VERSION_MAJOR=2.13
ARG WAR_URL=http://downloads.sourceforge.net/project/geoserver/GeoServer/${GS_VERSION}/geoserver-${GS_VERSION}-war.zip
ENV GEOSERVER_DATA_DIR $GEOSERVER_DATA_DIR
ENV ENABLE_JSONP true
ENV MAX_FILTER_RULES 20
ENV OPTIMIZE_LINE_WIDTH false
ENV GEOWEBCACHE_CACHE_DIR $GEOSERVER_DATA_DIR/gwc
ENV GEOSERVER_OPTS "-Djava.awt.headless=true -Xrs -XX:PerfDataSamplingInterval=500 \
 -Dorg.geotools.referencing.forceXY=true -XX:SoftRefLRUPolicyMSPerMB=36000 -XX:+UseParallelGC -XX:NewRatio=2 \
 -XX:+CMSClassUnloadingEnabled -Dfile.encoding=UTF8 -Duser.timezone=GMT -Djavax.servlet.request.encoding=UTF-8 \
 -Djavax.servlet.response.encoding=UTF-8 -Dorg.geotools.shapefile.datetime=true"
#-XX:+UseConcMarkSweepGC use this rather than parallel GC?
ENV JAVA_OPTS "$JAVA_OPTS $GEOSERVER_OPTS"
ENV GDAL_DATA /usr/local/gdal_data
ENV LD_LIBRARY_PATH /usr/local/gdal_native_libs:/usr/local/apr/lib:/opt/libjpeg-turbo/lib64
ENV GEOSERVER_LOG_LOCATION $GEOSERVER_DATA_DIR/logs/geoserver.log
ADD logs $GEOSERVER_DATA_DIR
ENV FOOTPRINTS_DATA_DIR /opt/footprints_dir
# Unset Java related ENVs since they may change with Oracle JDK
ENV JAVA_VERSION=
ENV JAVA_DEBIAN_VERSION=
# Set JAVA_HOME to /usr/lib/jvm/default-java and link it to OpenJDK installation
RUN ln -s /usr/lib/jvm/java-8-openjdk-amd64 /usr/lib/jvm/default-java
ENV JAVA_HOME /usr/lib/jvm/default-java
ARG ORACLE_JDK=false
ARG TOMCAT_EXTRAS=true
ARG COMMUNITY_MODULES=true

WORKDIR /tmp/
#ADD resources /tmp/resources
ADD scripts /scripts
ADD JDBC /JDBC
RUN chmod +x /scripts/*.sh
RUN /scripts/setup.sh
ADD scripts/controlflow.properties $GEOSERVER_DATA_DIR
ADD scripts/sqljdbc4-4.0.jar $CATALINA_HOME/webapps/geoserver/WEB-INF/lib/

# Clean up APT when done.
RUN echo "Yes, do as I say!" | apt-get remove --force-yes sed
RUN echo "Yes, do as I say!" | apt-get remove --force-yes login
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
&& dpkg --remove --force-depends build-essential

ENV JAVA_OPTS="${JAVA_OPTS} \
  -XX:+HeapDumpOnOutOfMemoryError \
  -XX:HeapDumpPath=/tmp/oom-heapdump.bin \
  -XshowSettings:vm \
  -Djava.security.egd=file:/dev/./urandom \
  -Dcom.sun.management.jmxremote.port=10999 \
  -Dcom.sun.management.jmxremote.rmi.port=10999 \
  -Dcom.sun.management.jmxremote.authenticate=false \
  -Dcom.sun.management.jmxremote.ssl=false"

CMD [ -n "$MEM_TOTAL_MB" ] && export JAVA_OPTS="-D__GEOSERVER__ -XX:MaxRAM=$(($MEM_TOTAL_MB * 70 / 100 - 75000000)) -XX:MaxRAMFraction=1 $JAVA_OPTS"; exec catalina.sh run
