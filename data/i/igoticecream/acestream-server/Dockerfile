#--------------------------------------------------------------
# Image: base
#--------------------------------------------------------------
FROM ubuntu:18.04

#--------------------------------------------------------------
# Image: information
#--------------------------------------------------------------
LABEL version="1.0" \
      maintainer="igoticecream@gmail.com" \
      description="Docker image for acestream engine server"

#--------------------------------------------------------------
# Install: Environment variables
#--------------------------------------------------------------
ENV DEBIAN_FRONTEND noninteractive
ENV ACESTREAM_HOME  /opt/acestream
ENV ACESTREAM_SRC   http://acestream.org/downloads/linux-beta/acestream_3.1.35_ubuntu_18.04_x86_64.tar.gz
ENV PATH            $ACESTREAM_HOME:$PATH

#--------------------------------------------------------------
# Install: Tools
#--------------------------------------------------------------
RUN apt-get update && \
    apt-get install --yes --quiet apt-utils && \
    apt-get install --yes --quiet --no-install-recommends \
        curl \
        wget \
        libpython2.7 \
        libssl1.0.0 \
        net-tools \
        python-minimal \
        python-pkg-resources \
        python-m2crypto \
        python-apsw \
        python-lxml \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

#--------------------------------------------------------------
# Install: Acestream
#--------------------------------------------------------------
WORKDIR $ACESTREAM_HOME
RUN     wget -qO - $ACESTREAM_SRC | tar -xzf -

#--------------------------------------------------------------
# Command
#--------------------------------------------------------------
CMD start-engine --client-console
