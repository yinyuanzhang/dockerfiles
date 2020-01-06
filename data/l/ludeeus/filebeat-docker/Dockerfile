# Base image
FROM alpine:3.9

# Copy root filesystem
COPY rootfs /

# ENV
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV FB_VERSION='6.7.1'
ENV FB_PATH=/usr/local/filebeat-"${FB_VERSION}"-linux-x86_64

# Add aloine 'edge/testing'
RUN echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

# Install packages
RUN apk add --no-cache \
    apk-tools=2.10.3-r1 \
    bash=4.4.19-r1 \
    curl=7.64.0-r1 \
    filebeat@edge \
    \
    && rm -f -r /tmp/* \
    \
    && curl -L -s https://github.com/just-containers/s6-overlay/releases/download/v1.21.7.0/s6-overlay-amd64.tar.gz \
        | tar xvzf - -C /


# Download and install Filebeat
RUN curl -L -s https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-oss-${FB_VERSION}-linux-x86_64.tar.gz \
    | tar xvzf - -C /usr/local 


# Fix premissions
RUN chmod go-w /etc/filebeat/filebeat.yml

# Entrypoint
ENTRYPOINT [ "/init" ]

# Arguments
ARG BUILD_DATE

# Labels
LABEL \
    maintainer="Joakim Sørensen @ludeeus <ludeeus@gmail.com>" \
    org.label-schema.description="Tasks." \
    org.label-schema.name="filebeat-docker" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/ludeeus/filebeat-docker" \
    org.label-schema.usage="https://github.com/ludeeus/filebeat-docker"