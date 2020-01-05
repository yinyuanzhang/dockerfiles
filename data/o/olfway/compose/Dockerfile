#
# Build image
#
ARG DEBIAN_IMAGE=debian:stretch-slim
FROM ${DEBIAN_IMAGE} as unpack

ENV LANG 'C.UTF-8'
ENV DEBIAN_FRONTEND=noninteractive

COPY --from=olfway/qemu-user-static /qemu-arm-static /usr/bin/
COPY --from=olfway/qemu-user-static /qemu-aarch64-static /usr/bin/

RUN set -x \
    && echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/zz-force-ipv4 \
    && echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/zz-no-install-recommends

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg2 \
        lsb-release

RUN set -x \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - \
    && echo "deb https://download.docker.com/linux/debian $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        python3-pip \
        python3-setuptools

WORKDIR /usr/src

ARG DOCKER_COMPOSE_RELEASE=1.21.2
RUN set -x \
    && curl -fsSL https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_RELEASE}/run.sh > run.sh \
    && curl -fsSL https://github.com/docker/compose/archive/${DOCKER_COMPOSE_RELEASE}.tar.gz > docker-compose.tar.gz

CMD [ "/bin/bash" ]

#
# Build image
#
FROM unpack as build

ARG IMAGE_NAME="olfway/compose:latest"

RUN set -x \
    && apt-get update \
    && apt-get install -y \
        docker-ce

WORKDIR /usr/src

COPY --from=unpack /usr/src/ /usr/src/

RUN set -x \
    && pip3 install --compile --no-binary :all: --no-cache-dir docker-compose.tar.gz

RUN set -x \
    && mkdir -p /usr/local/src \
    && cat run.sh | sed -r "/^VERSION=.*/d ; s#^IMAGE=.*#IMAGE='${IMAGE_NAME}'#" > /usr/local/src/run.sh

RUN set -x \
    && docker-compose --version

CMD [ "/bin/bash" ]

#
# Run image
#
FROM ${DEBIAN_IMAGE}
LABEL maintainer="Pavel Volkovitskiy <olfway@olfway.net>"

ENV LANG 'C.UTF-8'
ENV DEBIAN_FRONTEND=noninteractive

COPY --from=olfway/qemu-user-static /qemu-arm-static /usr/bin/
COPY --from=olfway/qemu-user-static /qemu-aarch64-static /usr/bin/

RUN set -x \
    && echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/zz-force-ipv4 \
    && echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/zz-no-install-recommends

RUN set -x \
    && apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install -y \
     	libltdl7 \
        python3 \
        python3-pkg-resources

COPY --from=build /usr/local/ /usr/local/
COPY --from=build /usr/bin/docker /usr/local/bin/

WORKDIR "/root"

RUN set -x \
    && uname -a \
    && docker --version \
    && docker-compose --version

COPY docker-compose-wrapper /usr/local/bin/

CMD [ ]
ENTRYPOINT [ "/bin/bash", "/usr/local/bin/docker-compose-wrapper" ]
