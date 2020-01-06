# Handbrake, compile hb.dll with aac-fdk support
# based on https://forum.videohelp.com/threads/383208-How-to-get-HandBrake-with-FDK-AAC-for-Windows
# and https://handbrake.fr/docs/en/latest/developer/build-windows.html
FROM ubuntu:latest

LABEL maintainer="docker@mbffm.de"
LABEL version="1.1.1"

# VARIABLES
ENV HANDBRAKE_VERSION latest
ENV HANDBRAKE_32BIT false
ENV UID 0
ENV GID 0

# CREATE FOLDER
RUN mkdir /app /data

# COPY FILE
COPY app.py /app

# UPDATE AND INSTALL DEPENDENCIES
RUN apt-get update && apt-get install -y \
	automake \
	autoconf \
	build-essential \
	cmake \
	curl \
	gcc \
	git \
	intltool \
	libtool \
	libtool-bin \
	m4 \
	make \
	nasm \
	patch \
	pkg-config \
	python \
	tar \
	yasm \
	zlib1g-dev \
# Install dependencies required to build the MinGW-w64 toolchain.
	bison \
	bzip2 \
	flex \
	g++ \
	gzip \
	pax \
# Additional for docker app.py
	python3 && \
# Cleanup
  rm -rf /var/lib/apt/lists/*

# VOLUME
VOLUME ["/data"]

# ENTRYPOINT
WORKDIR /app
CMD ["python3", "app.py"]
