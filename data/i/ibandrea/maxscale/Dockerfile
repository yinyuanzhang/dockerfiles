FROM centos:7

MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>

# MaxScale installation
RUN     rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB && \
        yum -y update && \
        yum -y install libedit libaio && \
        rpm -ivh https://downloads.mariadb.com/enterprise/bydh-zjmd/mariadb-maxscale/1.2/rhel/7/x86_64/maxscale-1.2.0-x86_64-rhel7.rpm && \
        yum clean all
ENV MAXSCALE_VERSION 1.2.0

# Move configuration file in directory for exports
RUN     mkdir -p /etc/maxscale.d && \
        mv /etc/maxscale.cnf /etc/maxscale.d && \
        ln -s /etc/maxscale.d/maxscale.cnf /etc/maxscale.cnf

# VOLUME for custom configuration
VOLUME ["/etc/maxscale.d"]

# Exposing the MaxScale default ports
## RW Split Listener
EXPOSE 4006

## Read Connection Listener
EXPOSE 4008

## Debug Listener
EXPOSE 4442

## CLI Listener
EXPOSE 6603

# Running MaxScale
ENTRYPOINT ["/bin/maxscale", "-d"]