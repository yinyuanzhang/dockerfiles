FROM openjdk:11-jdk-slim

ENV GDAL_VERSION 2.4.2
ENV ANT_VERSION 1.10.6

SHELL ["/bin/bash", "-ceux"]

# Build GDAL library
# The following files are the result of the compilation:
#   - /usr/share/java/gdal.jar
#   - /usr-local-lib.tgz (contains .so files, packaged as TAR due to Docker limitation with symlinks)

RUN TMP_DIR=/tmp/build && \
    DEBIAN_FRONTEND=noninteractive && \
    sed -i "s/\(deb\) \(.*\)/\1 \2\n\1-src \2/" /etc/apt/sources.list && \
    sed -i "s/ main$/ main contrib/" /etc/apt/sources.list && \
    apt-get -o Acquire::Check-Valid-Until=false update && \
    apt-get -y --no-install-recommends install curl unzip dselect build-essential autoconf libproj13 libproj-dev swig && \
    mkdir -p ${TMP_DIR} && \
    mkdir -p /usr/share/java/ && \
    cd ${TMP_DIR} && \
    curl -sSLk -o apache-ant.tar.gz https://www-eu.apache.org/dist//ant/binaries/apache-ant-${ANT_VERSION}-bin.tar.gz && \
    tar -xzf apache-ant.tar.gz -C /usr/local && \
    ln -s /usr/local/apache-ant-${ANT_VERSION}/ /usr/local/ant && \
    ANT_HOME=/usr/local/ant && \
    PATH=${PATH}:${ANT_HOME}/bin && \
    curl -sSL -o gdal-${GDAL_VERSION}.tar.gz https://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz && \
    tar xzf gdal-${GDAL_VERSION}.tar.gz && \
    cd gdal-${GDAL_VERSION} && \
    ./configure --with-java=/usr/local/openjdk-11 && \
    make -j$(nproc) && \
    make install && \
    cd swig/java && \
    make && \
    make install && \
    cp gdal.jar /usr/share/java/gdal.jar && \
    apt-get purge -y curl dselect build-essential autoconf libproj-dev swig && \
    apt-get autoremove -y && \
    apt-get clean && \
    cd / && \
    rm -rf ${TMP_DIR} /var/lib/apt-get/lists/* /usr/local/lib/*.a /usr/local/ant /usr/local/apache-ant* && \
    tar --absolute-names -zcf /usr-local-lib.tgz /usr/local/lib

