FROM leukgen/docker-cgpvcf:v0.1.0
LABEL maintainers="Juan S. Medina <https://github.com/jsmedmar>"

# install dependencies, make sure sh points to bash
ENV VERSION v3.3.0
COPY ./build/install_dependencies.sh /tmp
RUN bash /tmp/install_dependencies.sh && ln -sf /bin/bash /bin/sh

# create a /ifs volume for MSK users
VOLUME ["/data", "/gpfs", "/ifs"]
ENTRYPOINT [ "pindel.pl" ]
