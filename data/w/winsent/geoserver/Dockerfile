FROM ubuntu:trusty
MAINTAINER winsent<pipetc@gmail.com>


ENV DEBIAN_FRONTEND noninteractive
ENV GDAL_PATH /usr/local/share/gdal
ENV GEOSERVER_HOME /opt/geoserver
ENV GDAL_DATA $GDAL_PATH
ENV PATH $GDAL_PATH:$PATH
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/lib/jni:/usr/share/java

RUN export DEBIAN_FRONTEND=noninteractive
RUN dpkg-divert --local --rename --add /sbin/initctl

# Install packages
RUN \
  apt-get -y update --fix-missing && \
  apt-get -y install unzip software-properties-common && \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
  add-apt-repository -y ppa:webupd8team/java && \
  apt-get -y update && \
  apt-get install -y oracle-java8-installer && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/oracle-jdk8-installer && \
  rm -rf /tmp/* /var/tmp/*

ENV JAVA_HOME /usr/lib/jvm/java-8-oracle


ENV GDAL_VERSION 2.2.1
RUN apt-get -y update && apt-get -y install libproj-dev libjpeg-dev g++ make swig ant patch && \
# Install ECW 3.3
    wget http://www.kyngchaos.com/files/macosxport/libecwj2-3.3-2006-09-06.zip && \
    unzip libecwj2-3.3-2006-09-06.zip && \
    wget http://trac.osgeo.org/gdal/raw-attachment/ticket/3162/libecwj2-3.3-msvc90-fixes.patch && \
    patch -p0< libecwj2-3.3-msvc90-fixes.patch && \
    wget http://osgeo-org.1560.x6.nabble.com/attachment/5001530/0/libecwj2-3.3-wcharfix.patch && \
    wget http://trac.osgeo.org/gdal/raw-attachment/ticket/3366/libecwj2-3.3-NCSPhysicalMemorySize-Linux.patch && \
    cd libecwj2-3.3/ && \
    patch -p0< ../libecwj2-3.3-NCSPhysicalMemorySize-Linux.patch && \
    patch -p1< ../libecwj2-3.3-wcharfix.patch && \
    ./configure && \
    make && \
    make install && \
# Install GDAL
    wget http://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz -O /tmp/gdal.tar.gz && \
    tar xzf /tmp/gdal.tar.gz -C /tmp && \
    cd /tmp/gdal-${GDAL_VERSION} && ./configure  --with-java=$JAVA_HOME --with-ecw=/usr/local && \
    make && make install && \
    ldconfig && \
    ln -s /usr/local/bin/ogr2ogr /usr/bin/ogr2ogr && \
# Install GDAL Java binding
    cd /tmp/gdal-${GDAL_VERSION}/swig/java && \
    sed -i '/JAVA_HOME =/d' java.opt && \
    make && make install && \
    cp *.so /usr/local/lib/ && \
    mv /tmp/gdal-${GDAL_VERSION}/swig/java/gdal.jar /usr/share/gdal.jar && \
    apt-get purge -y g++ make swig ant patch && \
    rm -rf /tmp/*

ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib

# Get native JAI and ImageIO
RUN \
    cd $JAVA_HOME && \
    wget http://data.boundlessgeo.com/suite/jai/jai-1_1_3-lib-linux-amd64-jdk.bin && \
    echo "yes" | sh jai-1_1_3-lib-linux-amd64-jdk.bin && \
    rm jai-1_1_3-lib-linux-amd64-jdk.bin

RUN \
    cd $JAVA_HOME && \
    export _POSIX2_VERSION=199209 && \
    wget http://data.opengeo.org/suite/jai/jai_imageio-1_1-lib-linux-amd64-jdk.bin && \
    echo "yes" | sh jai_imageio-1_1-lib-linux-amd64-jdk.bin && \
    rm jai_imageio-1_1-lib-linux-amd64-jdk.bin

#
# GEOSERVER INSTALLATION
#
ENV GEOSERVER_VERSION 2.13.2

# Get GeoServer
RUN wget -c http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/geoserver-$GEOSERVER_VERSION-bin.zip -O ~/geoserver.zip && \
    unzip ~/geoserver.zip -d /opt && mv -v /opt/geoserver* $GEOSERVER_HOME && \
    rm ~/geoserver.zip

# Get OGR plugin
RUN wget -c http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-ogr-wfs-plugin.zip -O ~/geoserver-ogr-plugin.zip && \
    unzip -o ~/geoserver-ogr-plugin.zip -d $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/ && \
    rm ~/geoserver-ogr-plugin.zip
    
# Get GDAL plugin
RUN wget -c http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-gdal-plugin.zip -O ~/geoserver-gdal-plugin.zip && \
    unzip -o ~/geoserver-gdal-plugin.zip -d $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/ && \
    rm ~/geoserver-gdal-plugin.zip

# Get printing plugin
RUN wget -c http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-printing-plugin.zip -O ~/geoserver-printing-plugin.zip && \
    unzip ~/geoserver-printing-plugin.zip -d $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/ && \
    rm ~/geoserver-printing-plugin.zip

# Get import plugin
RUN wget -c http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-importer-plugin.zip -O ~/geoserver-importer-plugin.zip && \
    unzip -o ~/geoserver-importer-plugin.zip -d $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/ && \
    rm ~/geoserver-importer-plugin.zip

# Get vector tiles plugin
RUN wget -c http://downloads.sourceforge.net/project/geoserver/GeoServer/$GEOSERVER_VERSION/extensions/geoserver-$GEOSERVER_VERSION-vectortiles-plugin.zip -O ~/geoserver-vectortiles-plugin.zip && \
    unzip -o ~/geoserver-vectortiles-plugin.zip -d $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/ && \
    rm ~/geoserver-vectortiles-plugin.zip

# Replace GDAL Java bindings
RUN rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/imageio-ext-gdal-bindings-1.9.2.jar
RUN cp /usr/share/gdal.jar $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/gdal.jar

# Remove old JAI from geoserver
RUN rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/jai_codec-1.1.3.jar && \
    rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/jai_core-1.1.3.jar && \
    rm -rf $GEOSERVER_HOME/webapps/geoserver/WEB-INF/lib/jai_imageio-1.1.jar

# Enable JAI-EXT
RUN sed -i '/-jar start.jar/ s/$/-Dorg.geotools.coverage.jaiext.enabled=true/' /opt/geoserver/bin/startup.sh

# Set default locale
ENV LANG C.UTF-8

# Expose GeoServer's default port
EXPOSE 8080
CMD ["/opt/geoserver/bin/startup.sh"]

