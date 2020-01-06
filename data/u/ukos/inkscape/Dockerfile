FROM debian
MAINTAINER Matthias J. Kastner matthias@project-moby.net

RUN apt-get update && \
	apt-get install --no-install-recommends --assume-yes \
		git \
		libheif-examples \
		inkscape \
		imagemagick && \
	apt-get clean
