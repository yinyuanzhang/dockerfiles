FROM alpine:edge
MAINTAINER Joe Izzard

ARG BUILD_DATE
ARG VCS_REF

LABEL  org.label-schema.build-date=$BUILD_DATE \
        org.label-schema.schema-version="1.0.0-rc1" \
        org.label-schema.name="MilliAlpine" \
        org.label-schema.description="A lightweight and complete Alpine image"\
        org.label-schema.version="edge"\
        org.label-schema.url="https://izzard.dev/docker/millialpine"\
        org.label-schema.usage="https://izzard.dev/docker/millialpine/v3.10.2/usage"\
        org.label-schema.vcs-url="https://github.com/JoeIzzard/MilliAlpine"\
        org.label-schema.vcs-ref=$VCS_REF

RUN \

    # Update and Upgrade
    apk update && apk upgrade && \

    # Install Packages
    apk add ca-certificates tzdata bash logrotate && \

    # Build the file structure
    mkdir /Server && \
    ln -s /var/log /Server/Logs

CMD ["/bin/sh"]