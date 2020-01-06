FROM leukgen/docker-pcapcore:v0.1.1
LABEL maintainers="Juan S. Medina <https://github.com/jsmedmar>"

# install dependencies, make sure sh points to bash
ENV VERSION v2.0.4
COPY ./build/install_dependencies.sh /tmp
RUN bash /tmp/install_dependencies.sh && ln -sf /bin/bash /bin/sh

# create a /ifs volume for MSK users
VOLUME ["/data", "/gpfs", "/ifs"]
ENTRYPOINT []
