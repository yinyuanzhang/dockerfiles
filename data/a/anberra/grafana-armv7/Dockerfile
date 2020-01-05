FROM balenalib/armv7hf-debian

# author
MAINTAINER andres.bermejo@gmail.com

# extra metadata
LABEL version="6.5.0"
LABEL description="Image with Grafana for armv7"
ADD VERSION .

# variables
ARG PKG_NAME="6.5.0"
ARG GF_UID="472"
ARG GF_GID="472"
ARG DEB_FILE="grafana_${PKG_NAME}_armhf.deb"

# env
ENV GRAFANA_URL="https://dl.grafana.com/oss/release/$DEB_FILE" \
    PATH=/usr/share/grafana/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    GF_PATHS_CONFIG="/etc/grafana/grafana.ini" \
    GF_PATHS_DATA="/var/lib/grafana" \
    GF_PATHS_HOME="/usr/share/grafana" \
    GF_PATHS_LOGS="/var/log/grafana" \
    GF_PATHS_PLUGINS="/var/lib/grafana/plugins" \
    GF_PATHS_PROVISIONING="/etc/grafana/provisioning" \
    GF_PATHS_DEB="/depot"

# cross-build to build arm containers on dockerhub
RUN [ "cross-build-start" ]

# install basics
RUN apt-get update && apt-get install -y \
        curl \
        libfontconfig \
        && rm -rf /var/lib/apt/lists/*

# deploy
RUN mkdir -p "$GF_PATHS_HOME/.aws" && \
    mkdir -p "$GF_PATHS_DEB" && \
    groupadd -r -g $GF_GID grafana && \
    useradd -r -u $GF_UID -g grafana grafana && \
    mkdir -p "$GF_PATHS_PROVISIONING/datasources" \
             "$GF_PATHS_PROVISIONING/dashboards" \
             "$GF_PATHS_PROVISIONING/notifiers" \
             "$GF_PATHS_LOGS" \
             "$GF_PATHS_PLUGINS" \
             "$GF_PATHS_DATA" && \
    chown -R grafana:grafana "$GF_PATHS_DATA" "$GF_PATHS_HOME/.aws" "$GF_PATHS_LOGS" "$GF_PATHS_PLUGINS" && \
    chmod 777 "$GF_PATHS_DATA" "$GF_PATHS_HOME/.aws" "$GF_PATHS_LOGS" "$GF_PATHS_PLUGINS" "$GF_PATHS_PROVISIONING/notifiers" "$GF_PATHS_PROVISIONING" && \
    curl -L "$GRAFANA_URL" --output "$GF_PATHS_DEB/$DEB_FILE" && \ 
    dpkg -i "$GF_PATHS_DEB/$DEB_FILE" && \
    cp "$GF_PATHS_HOME/conf/sample.ini" "$GF_PATHS_CONFIG" && \
    cp "$GF_PATHS_HOME/conf/ldap.toml" /etc/grafana/ldap.toml && \
    rm "$GF_PATHS_DEB/$DEB_FILE"

# timezone
RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Madrid /etc/localtime

# cross-build to build arm containers on dockerhub
RUN [ "cross-build-end" ]

EXPOSE 3000

COPY ./run.sh /run.sh

USER grafana
WORKDIR /
ENTRYPOINT [ "/run.sh" ]
