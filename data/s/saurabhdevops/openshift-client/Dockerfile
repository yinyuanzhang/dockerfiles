FROM frolvlad/alpine-glibc:latest

MAINTAINER "Saurabh Oza" <saurabh.devops@gmail.com>

# specify the version string of the oc release
ENV OC_VERSION "v3.9.0"
ENV OC_RELEASE "openshift-origin-client-tools-v3.9.0-191fece-linux-64bit"



# install the oc client tools
ADD https://github.com/openshift/origin/releases/download/$OC_VERSION/$OC_RELEASE.tar.gz /opt/oc/release.tar.gz
RUN apk add --no-cache ca-certificates
RUN tar --strip-components=1 -xzvf  /opt/oc/release.tar.gz -C /opt/oc/ && \
    mv /opt/oc/oc /usr/bin/ && \
    rm -rf /opt/oc

EXPOSE 8001

RUN apk update && \
    apk add --no-cache \
                bash \
                git \
                curl \
                ca-certificates \
                openssl

ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 17.03.1-ce
ENV DOCKER_SHA256 820d13b5699b5df63f7032c8517a5f118a44e2be548dd03271a86656a544af55

RUN set -x \
        && mkdir -p /tmp/docker \
	&& curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o /tmp/docker/docker.tgz \
	&& sha256sum /tmp/docker/docker.tgz  | grep $DOCKER_SHA256 \
	&& tar -xzvf /tmp/docker/docker.tgz -C /tmp/docker/ \
	&& mv /tmp/docker/docker/* /usr/local/bin/ \
	&& rm -rf /tmp/docker \
	&& docker -v
