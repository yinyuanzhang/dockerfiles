FROM alpine:latest

LABEL \
    maintainer="Morgan AUCHEDE <morgan.auchede@gmail.com>"

RUN set -e -u -x \
\
    # Install packages
\
    && apk add --no-cache --no-progress --virtual BUILD_DEPS curl \
    && apk add --no-cache --no-progress bash openssl \
\
    # Install dumb-entrypoint
\
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/dumb-entrypoint/installer" | bash -s -- install \
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/gosu/installer" | bash -s -- install \
\
    # Install omgwtfssl
\
    && curl --location --output /usr/bin/generate-certs "https://github.com/paulczar/omgwtfssl/raw/master/generate-certs" \
    && chmod +x /usr/bin/generate-certs \
\
    # Clean
\
    && apk del --no-progress BUILD_DEPS

ENTRYPOINT [ "dumb-entrypoint" ]
