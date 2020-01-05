FROM leukgen/docker-cgpvcf:v0.1.0

RUN \
    # install packages dependencies
    apt-get update -yqq && \
    apt-get install -yqq python-pip && \
    apt-get clean

# install dependencies, make sure sh points to bash
ENV CGP_BATTENBERG_VERSION v3.3.0
ENV ALLELE_COUNT_VERSION v4.0.0
ENV IMPUTE2_VERSION v2.3.2

COPY ./build/install_dependencies.sh /tmp
RUN bash /tmp/install_dependencies.sh && ln -sf /bin/bash /bin/sh

# create a /ifs volume for MSK users
VOLUME ["/data", "/gpfs", "/ifs"]
ENTRYPOINT [ "battenberg.pl" ]
