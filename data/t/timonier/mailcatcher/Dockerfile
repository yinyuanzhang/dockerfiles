FROM ruby:2.3-alpine

LABEL \
    maintainer="Morgan AUCHEDE <morgan.auchede@gmail.com>"

RUN set -e -u -x \
\
    # Install packages
\
    && apk add --no-cache --no-progress --virtual BUILD_DEPS build-base ca-certificates curl gmp-dev sqlite-dev \
    && apk add --no-cache --no-progress bash gmp libstdc++ sqlite-libs \
\
    # Install dumb-entrypoint
\
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/dumb-entrypoint/installer" | bash -s -- install \
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/gosu/installer" | bash -s -- install \
\
    # Install mailcatcher
\
    && gem install --no-verbose mailcatcher \
\
    # Clean
\
    && apk del --no-progress BUILD_DEPS \
    && rm -f -r /root/.gem /tmp/*

ENTRYPOINT [ "dumb-entrypoint" ]
