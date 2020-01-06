FROM alpine:latest

LABEL \
    maintainer="Morgan AUCHEDE <morgan.auchede@gmail.com>"

ENV \
    GITEA_WORK_DIR=/var/lib/gitea \
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    S6_KEEP_ENV=1 \
    S6_READ_ONLY_ROOT=1

RUN set -e -u -x \
\
    # Install packages
\
    && apk add --no-cache --no-progress --virtual BUILD_DEPS curl \
    && apk add --no-cache --no-progress bash git openssh-client shadow \
\
    # Create git user
\
    && adduser -D -g "Git Version Control" -h "${GITEA_WORK_DIR}" git git \
\
    # Install dockerize
\
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/dockerize/installer" | bash -s -- install \
\
    # Install gitea
\
    && export $(curl --location "https://gitlab.com/timonier/version-lister/raw/generated/go-gitea/gitea/latest" | xargs) \
    && curl --location --output /usr/local/bin/gitea "${GITEA_RELEASE}" \
    && chmod +x /usr/local/bin/gitea \
\
    # Install s6-overlay
\
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/s6-overlay/installer" | bash -s -- install \
\
    # Clean
\
    && apk del --no-progress BUILD_DEPS \
    && rm -f -r /tmp/*

COPY rootfs/ /

ENTRYPOINT [ "/init" ]
