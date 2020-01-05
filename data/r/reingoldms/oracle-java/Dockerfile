FROM centos:7
MAINTAINER Kevin Harris <kharris@reingold.com>
MAINTAINER Kevin Chabreck <kchabreck@reingold.com>

# Builds an image containing CentOS 7 and an Oracle Java JDK
# note: Java is installed to /opt/java_home

#crazy hash is in the url, not sure if it changes?
ENV JAVA_DOWNLOAD_URL http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/
ENV JAVA_ARCHIVE_FILENAME jdk-8u181-linux-x64.tar.gz

 # install wget
RUN yum -y update && \
    yum -y install wget && \
    yum -y clean all

# install Oracle Java JDK
RUN wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" ${JAVA_DOWNLOAD_URL}${JAVA_ARCHIVE_FILENAME} && \
    mkdir /opt/java_home && \
    tar xf ${JAVA_ARCHIVE_FILENAME} -C /opt/java_home --strip-components 1 && \
    rm ${JAVA_ARCHIVE_FILENAME}

# define commonly used JAVA_HOME variable
ENV JAVA_HOME /opt/java_home
ENV PATH ${PATH}:/opt/java_home/bin
