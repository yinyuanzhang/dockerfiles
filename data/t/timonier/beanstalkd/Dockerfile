FROM debian:stable-slim

LABEL \
    maintainer="Morgan AUCHEDE <morgan.auchede@gmail.com>"

RUN set -e -u -x \
\
    # Prepare system
\
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
\
    # Install packages
\
    && BUILD_DEPS="build-essential curl" \
    && apt-get install --no-install-recommends --yes ${BUILD_DEPS} ca-certificates locales \
\
    # Install beanstalkd
\
    && export $(curl --location "https://gitlab.com/timonier/version-lister/raw/generated/kr/beanstalkd/latest" | xargs) \
    && curl --location "${BEANSTALKD_SOURCE}" | tar --directory /tmp --extract --gzip \
    && make --directory /tmp/beanstalkd-"${BEANSTALKD_VERSION}" \
    && make --directory /tmp/beanstalkd-"${BEANSTALKD_VERSION}" install \
\
    # Install dumb-entrypoint
\
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/dumb-entrypoint/installer" | bash -s -- install \
    && curl --location "https://gitlab.com/timonier/dumb-entrypoint/raw/master/src/gosu/installer" | bash -s -- install \
\
    # Clean
\
    && apt-get remove --purge --yes ${BUILD_DEPS} \
    && apt-get autoremove --purge --yes \
    && rm -f -r /tmp/* /var/lib/apt/lists/*

ENTRYPOINT [ "dumb-entrypoint" ]
