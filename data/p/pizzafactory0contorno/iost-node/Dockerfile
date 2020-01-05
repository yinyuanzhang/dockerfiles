ARG BASE_TAG
FROM iostio/iost-node:${BASE_TAG}

# Eclipse/Che uses here for the project root.
VOLUME /projects
WORKDIR /projects

env HOME /projects

# The runtime user can be non root.
RUN mkdir -p /var/lib/iserver/ /.iwallet/ && \
    chgrp -R 0 /var/lib/iserver/ /.iwallet/ /projects && \
    chmod g+rwX /var/lib/iserver/ /.iwallet/ /projects

