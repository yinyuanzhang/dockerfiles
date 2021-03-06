#################################################################
# Dockerfile
#
# Version:          1
# Software:         APERIM Distance2Self
# Website:          http://aperim.eu
# Tags:             distance2self
# Provides:         APERIM
# Base Image:       aperim/baseimage
# Build Cmd:        docker build -t aperim/distance2self .
# Pull Cmd:         docker pull aperim/distance2self
# Run Cmd:          todo eg. docker run centos:[localname] tools
# Extra:            Base image to provide bioinformatic tools for
# Extra:            academical use
#################################################################

# Set the base image to biodocker base image
FROM aperim/baseimage

# update os, install prequisites and clean cache
RUN yum clean all && yum -y install epel-release && yum -y update \
&& yum -y install \
    boost-devel \
    boost-serialization \
    glpk-utils \
    git \
    python-pip \
    python-devel \
    mysql-devel \
&& rm -rf /tmp/* /var/tmp/* ~/.cache/*

################## BEGIN INSTALLATION ######################
#python stuff
RUN pip install --upgrade pip \
&& pip install git+https://github.com/FRED-2/Fred2@master

RUN git clone https://github.com/APERIM-EU/WP3-Distance2Self.git \
    && chmod -R 777 /WP3-Distance2Self/ \
    && cd /WP3-Distance2Self/src \
    && make

ENV PATH /WP3-Distance2Self/:$PATH

# create shared folders
RUN mkdir /data /config

# Add user aperim with password aperim
#RUN useradd --create-home --shell /bin/bash --user-group --uid 1000 --groups sudo,fuse aperim && \
#    echo `echo "aperim\aperim\n" | passwd aperim` && \
#    chown aperim:aperim /data && \
#    chown aperim:aperim /config

# Change user
#USER biodocker

# Share default volumes
VOLUME ["/data", "/config"]

# Overwrite this with 'CMD []' in a dependent Dockerfile
ENTRYPOINT ["Distance2Self.py"]
CMD ["-h"]

# change workdir
WORKDIR /data
##################### INSTALLATION END #####################

# File Author / Maintainer
MAINTAINER Benjamin Schubert <schubert@informatik.uni-tuebingen.de>
# Modified by Felipe da Veiga Leprevost 08-09-2016