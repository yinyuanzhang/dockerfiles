# Base image
FROM alpine:3.9

# Copy root filesystem
COPY rootfs /

# ENV
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2
ENV PYTHONUNBUFFERED=0

# Build
RUN \
    apk add --no-cache \
    apk-tools=2.10.3-r1 \
    bash=4.4.19-r1 \
    curl=7.64.0-r1 \
    python3=3.6.8-r1 \
    \
    && rm -f -r /tmp/* \
    \
    && curl -L -s https://github.com/just-containers/s6-overlay/releases/download/v1.21.7.0/s6-overlay-amd64.tar.gz \
        | tar xvzf - -C / \
    \
    && python3 -m pip install -U pip \
    \
    && python3 -m pip install repoupdater customjson addonupdater

# Entrypoint
ENTRYPOINT [ "/init" ]

# Arguments
ARG BUILD_DATE

# Labels
LABEL \
    maintainer="Joakim Sørensen @ludeeus <ludeeus@gmail.com>" \
    org.label-schema.description="Tasks." \
    org.label-schema.name="tasks" \
    org.label-schema.schema-version="1.0" \
    org.label-schema.url="https://github.com/ludeeus/tasks" \
    org.label-schema.usage="https://github.com/ludeeus/tasks"