FROM centos:7.4.1708
MAINTAINER kinumi

# install vlc
RUN yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm
RUN yum install -y vlc

# install other packages
RUN yum install -y wget bzip2

# install Air Video Server HD for Linux
RUN mkdir /app
WORKDIR /app
RUN wget "https://s3.amazonaws.com/AirVideoHD/Download/AirVideoServerHD-2.2.3.tar.bz2" \
    && tar xfj "AirVideoServerHD-2.2.3.tar.bz2"

# add files
ADD Server.properties ./
ADD start.sh ./


## -- Run AirVideoServerHD under Tini --

# Add Tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Run your program under Tini
CMD ["/bin/sh", "/app/start.sh"]


## -- META DATA --

EXPOSE 45633
VOLUME ["/config", "/video"]
