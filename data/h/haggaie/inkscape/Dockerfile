FROM debian:stretch

RUN echo deb http://deb.debian.org/debian stretch contrib > /etc/apt/sources.list.d/contrib.list
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install \
    ca-certificates \
	inkscape \
	ttf-mscorefonts-installer

WORKDIR /document
ENTRYPOINT ["inkscape"]
