FROM alpine:latest
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>

# install packages &
## OpenZwave installation &
# grep git version of openzwave &
# untar the files &
# compile &
# "install" in order to be found by domoticz &
## Domoticz installation &
# clone git source in src &
# Domoticz needs the full history to be able to calculate the version string &
# prepare makefile &
# compile &
# remove git and tmp dirs

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/domoticz/domoticz" \
      org.label-schema.url="https://domoticz.com/" \
      org.label-schema.name="Domoticz" \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.license="GPLv3" \
      org.label-schema.build-date=$BUILD_DATE

RUN apk add --no-cache git \
	 git \
	 python3 python3-dev \
	 libssl1.0 libressl-dev \
	 build-base cmake \
	 boost-dev \
	 boost-thread \
	 boost-system \
	 boost-date_time \
	 sqlite sqlite-dev \
	 curl libcurl curl-dev \
	 libusb libusb-dev \
	 coreutils tzdata \
	 zlib zlib-dev wget python3 python3-dev \
	 udev eudev-dev \
	 linux-headers && \
	 git clone --depth 2 https://github.com/OpenZWave/open-zwave.git /src/open-zwave && \
	 cd /src/open-zwave && \
	 make && \
	 ln -s /src/open-zwave /src/open-zwave-read-only && \
	 git clone -b 4.9700  --depth 2 https://github.com/domoticz/domoticz.git /src/domoticz && \
	 cd /src/domoticz && \
	 git fetch --unshallow && \
	 cmake -DCMAKE_BUILD_TYPE=Release . && \
	 make && \
	 rm -rf /src/domoticz/.git && \
	 rm -rf /src/open-zwave/.git && \
	 apk del git cmake python3-dev linux-headers libusb-dev zlib-dev libressl-dev boost-dev sqlite-dev build-base eudev-dev coreutils curl-dev

VOLUME /config

EXPOSE 8080

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:8080/ || exit 1

ENTRYPOINT ["/src/domoticz/domoticz", "-dbase", "/config/domoticz.db"]
CMD ["-www", "8080"]
