FROM grafana/grafana

ENV VERSION 7.5.0-b1

USER root

# install sudo/sudoers
RUN apt-get update \
    && apt-get install -y sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && echo "grafana ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers

# install plugin
COPY dists/grafana-baas-object-datasource-$VERSION.tar.gz /tmp

RUN cd /var/lib/grafana/plugins \
    && tar xvzf /tmp/grafana-baas-object-datasource-$VERSION.tar.gz \
    && mv grafana-baas-object-datasource-$VERSION grafana-baas-object-datasource

USER grafana

#ENTRYPOINT /bin/bash
