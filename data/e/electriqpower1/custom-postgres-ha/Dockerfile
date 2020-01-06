# The electriq Postgres image
FROM electriqpower1/custom-postgres:1.2.0@sha256:2a6010831d5d2e583aa120de4db55e929c591d8cf72908ff4b8c3a4cbf773c59

MAINTAINER Elctriq Power https://electriqpower.com

# Expose database port
EXPOSE 5432

# Install gcloud & productivity tools
RUN CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" \
  && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" \
    | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
    | apt-key add - \
  && apt-get update -qq \
  && apt-get install -yq google-cloud-sdk zsh tmux

# Add stolon user
RUN useradd -ms /bin/bash stolon

# Install stolon binaries
ENV STOLON_VERSION ${STOLON_VERSION:-0.13.0}
RUN mkdir -p /tmp
WORKDIR /tmp
RUN wget https://github.com/sorintlab/stolon/releases/download/v$STOLON_VERSION/stolon-v$STOLON_VERSION-linux-amd64.tar.gz
RUN tar -xvf stolon-v$STOLON_VERSION-linux-amd64.tar.gz

WORKDIR /tmp/stolon-v0.13.0-linux-amd64/bin/
RUN mv stolon* /usr/local/bin/

RUN chmod +x /usr/local/bin/stolon-keeper /usr/local/bin/stolon-sentinel /usr/local/bin/stolon-proxy /usr/local/bin/stolonctl

WORKDIR /
