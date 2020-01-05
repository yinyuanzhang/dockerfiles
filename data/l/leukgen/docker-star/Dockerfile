FROM ubuntu:16.04
LABEL maintainers="Juan S. Medina <https://github.com/jsmedmar>"

# install all dependencies in OPT
ENV VERSION 2.5.4b
ENV OPT /opt/star
ENV PATH $OPT/bin/Linux_x86_64:$PATH

# install dependencies, make sure sh points to bash
COPY ./build/install_dependencies.sh /tmp
RUN bash /tmp/install_dependencies.sh && ln -sf /bin/bash /bin/sh

# set locale
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

# create a /ifs and /gpfs volume for MSK users
VOLUME /ifs
VOLUME /gpfs
VOLUME /data
WORKDIR /data
ENTRYPOINT [ "STAR" ]
