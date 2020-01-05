FROM centos:centos7

LABEL name="CentOS Base Image"
LABEL vendor="CentOS"
LABEL license=GPLv2

ENV REFRESHED_AT 2016-09-09

# - Install basic packages (e.g. python-setuptools is required to have python's easy_install)
# - Install yum-utils so we have yum-config-manager tool available
# - Install inotify, needed to automate daemon restarts after config file changes
# - Install jq, small library for handling JSON files/api from CLI
# - Install supervisord (via python's easy_install - as it has the newest 3.x version)

RUN yum update -y && \
    yum install -y epel-release && \
    yum install -y unzip iproute python-setuptools hostname inotify-tools yum-utils which jq python-pip && \
    
    # Salt and prerequisites
    yum install -y salt-minion virt-what && \

    # Additional tools
    yum install -y net-tools nmap git && \
        
    # Clean Up
    yum clean all && \
    
    # Supervisor 
    easy_install supervisor
    
#Install JRE
ENV JRE_VERSION 8u31
ENV JRE_CHECKSUM 4d6a99aa7f2addde8f6ad714e788ff61
ENV JAVA_HOME /usr/java/latest 

# Download and install the required version of Oracle's JDK 
RUN yum install -y wget && \
    wget --quiet --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/$JRE_VERSION-b13/jre-$JRE_VERSION-linux-x64.rpm" && \
    echo "$JRE_CHECKSUM  jre-$JRE_VERSION-linux-x64.rpm" >> MD5SUM && \
    md5sum -c MD5SUM && \
    yum install -y "jre-$JRE_VERSION-linux-x64.rpm" && \
    yum clean all && \
    yum -y remove wget && \
    rm -rf "jre-$JRE_VERSION-linux-x64.rpm" \
           MD5SUM && \
    update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 999999 

# Download and install Mule
ENV MULE_HOME /opt/mule
ENV MULE_VERSION 3.8.0
RUN set -x \
        && cd /opt \
        && curl -o mule.zip -H "Authorization: Basic Y2lzY28ubmV4dXM6YzNScjRyUDBkcjRtMTVvSjBz" https://repository.mulesoft.org/nexus/content/repositories/releases-ee/com/mulesoft/muleesb/distributions/mule-ee-distribution-standalone/$MULE_VERSION/mule-ee-distribution-standalone-$MULE_VERSION.zip \
        && unzip mule.zip \
        && mv mule-enterprise-standalone-$MULE_VERSION mule \
        && rm mule.zip* \
        && find . -name "*freebsd*.*" -type f -delete \
        && find . -name "*aix*.*" -type f -delete \
        && find . -name "*hpux*.*" -type f -delete \
        && find . -name "*solaris*.*" -type f -delete \
        && find . -name "*macosx*.*" -type f -delete \
        && find . -name "*windows*.*" -type f -delete 
        
# -- START - UNCOMMENT THIS IF YOU HAVE A ENTERPRISE LICENSE --

## Move Enterprise License Key for Mule 
#COPY srv/mule/muleLicenseKey.lic /opt/mule/license/license.lic

# -- END - UNCOMMENT THIS IF YOU HAVE A ENTERPRISE LICENSE --

# Moving Runtime Configuration for Main Components - Supervisor and Salt Minion 
ADD etc	     /etc 
ADD config   /config
ADD etc/mule/shared-domain.zip   /opt/mule/apps/shared-domain.zip

RUN mkdir -p /var/log/supervisor

# Expose volumes
VOLUME ["/var/log/supervisor"]

# Exposing Proxy ports
EXPOSE 8081

RUN ["chmod", "+x", "/config/bootstrap.sh"]
RUN ["chmod", "+x", "/config/init/configureenv.sh"]
RUN ["chmod", "+x", "/config/init/setupminion.sh"]

#Running the Start Script
CMD ["/config/bootstrap.sh"]
