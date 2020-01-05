FROM leukgen/docker-cgpvcf:v0.1.0

RUN \
    # install packages dependencies
    apt-get update -yqq && \
    apt-get install -yqq python-pip && \
    apt-get clean

# install dependencies, make sure sh points to bash
# ENV POST_PROCESSING_VERSION 1.7.0
# ENV WRAPPER_VERSION 1.11.1
ENV POST_PROCESSING_VERSION 1.8.2
ENV WRAPPER_VERSION 1.13.2

COPY ./build/install_dependencies.sh /tmp
RUN bash /tmp/install_dependencies.sh && ln -sf /bin/bash /bin/sh

# create a /ifs volume for MSK users
VOLUME ["/data", "/gpfs", "/ifs"]
ENTRYPOINT [ "caveman.pl" ]
