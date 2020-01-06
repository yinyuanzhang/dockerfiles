FROM alpine:3.10
LABEL maintainer="Lanestolen"

ARG OVERLAY_VERSION="v1.22.1.0"
ARG OVERLAY_ARCH="amd64"

RUN \
echo "**** install runtime packages ****" && \
apk add --no-cache \
    netcat-openbsd \
	bash \
	ca-certificates \
	coreutils \
	shadow \
	tzdata && \
echo "**** create abc user and make our folders ****" && \
groupmod -g 1000 users && \
useradd -u 911 -U -d /config -s /bin/false abc && \
usermod -G users abc && \
mkdir -p \
    /app \
	/config \
	/defaults

# Add s6-overlay
RUN wget https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz -O /tmp/s6-overlay.tar.gz && \
    tar xzf /tmp/s6-overlay.tar.gz -C / && \
    rm -r /tmp/s6-overlay.tar.gz

# Remove temporary
RUN rm -rf \
    /tmp/*

# Add files
COPY root/ /

ENTRYPOINT ["/init"]
