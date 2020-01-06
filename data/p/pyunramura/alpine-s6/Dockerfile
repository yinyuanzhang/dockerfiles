FROM scratch
ADD rootfs.tar.xz /

ARG OVERLAY_VERSION
ARG OVERLAY_ARCH
ARG BUILD_DATE
ARG VCS_REF
ARG VCS_URL
ARG VERSION

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-ref="$VCS_REF" \
      org.label-schema.vcs-url="$VCS_URL" \
      org.label-schema.version="$VERSION" \
      org.label-schema.maintainer="pyunramura"

# environment variables
ENV PS1="$(whoami)@$(hostname):$(pwd)$ " \
HOME="/root" \
TERM="xterm"

RUN \
 echo "---- installing build dependencies ----" && \
  apk add --update --virtual=virtual-dependencies \
	curl \
	tar && \
 echo "---- installing base usability packages ----" && \
 apk add --no-cache \
	coreutils=8.29-r2 \
        curl=7.61.1-r1 \
	shadow=4.5-r0 && \
 echo "---- adding s6-overlay ----" && \
 curl -o \
 /tmp/s6-overlay.tar.gz -L \
	"https://github.com/just-containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz" && \
 tar xfz \
	/tmp/s6-overlay.tar.gz -C / && \
 echo "---- creating abc user and making folders ----" && \
 groupmod -g 1000 users && \
 useradd -r -u 783 -U -d /config -s /bin/false abc && \
 usermod -G users abc && \
 mkdir -p \
	/app \
	/config \
	/defaults && \
 echo "---- taking out the trash ----" && \
 apk del --purge \
	virtual-dependencies && \
 rm -rf \
	/tmp/* /var/cache/apk/*

# add local files
COPY root/ /

ENTRYPOINT ["/init"]
