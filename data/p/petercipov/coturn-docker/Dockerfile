FROM debian:9.4-slim
ARG CORURN_VERSION=4.5.0.5-1+deb9u1
RUN apt-get update -q && \
    apt-get install -q -y coturn=${CORURN_VERSION}

ENTRYPOINT [ "/usr/bin/turnserver" ]