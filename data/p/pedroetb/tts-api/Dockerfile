ARG NODE_IMAGE_TAG=12.6-stretch-slim

FROM node:${NODE_IMAGE_TAG}

LABEL maintainer="pedroetb@gmail.com"

ARG APT_REPOSITORY="deb http://ftp.de.debian.org/debian stretch main non-free"

ARG GOOGLE_SPEECH_VERSION=1.1.0
ARG GTTS_VERSION=2.0.3
ARG ESPEAK_VERSION=1.48.04+dfsg-5+b1
ARG FESTIVAL_VERSION=1:2.4~release-3+b1

ARG PYTHON3_VERSION=3.5.3-1
ARG PYTHON3_PIP_VERSION=9.0.1-2+deb9u1
ARG PYTHON3_SETUPTOOLS_VERSION=33.1.1-1
ARG PYTHON3_WHEEL_VERSION=0.29.0-2
ARG SOX_VERSION=14.4.1-5+deb9u2
ARG LIBSOX_FMT_MP3_VERSION=14.4.1-5+deb9u2
ARG FESTVOX_ELLPC11K_VERSION=1.4.0-4

RUN echo ${APT_REPOSITORY} >> /etc/apt/sources.list && \
	apt-get update && \
	apt-get install --no-install-recommends -y \
		python3=${PYTHON3_VERSION} \
		python3-pip=${PYTHON3_PIP_VERSION} \
		python3-setuptools=${PYTHON3_SETUPTOOLS_VERSION} \
		python3-wheel=${PYTHON3_WHEEL_VERSION} \
		sox=${SOX_VERSION} \
		libsox-fmt-mp3=${LIBSOX_FMT_MP3_VERSION} \
		festival=${FESTIVAL_VERSION} \
		festvox-ellpc11k=${FESTVOX_ELLPC11K_VERSION} \
		espeak=${ESPEAK_VERSION} && \
	pip3 install \
		google_speech==${GOOGLE_SPEECH_VERSION} \
		gTTS==${GTTS_VERSION} && \
	apt-get remove --purge -y \
		python3-pip \
		python3-setuptools \
		python3-wheel && \
	apt-get autoremove --purge -y && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /tts-api

COPY package.json package-lock.json ./
COPY app/ ./app/
COPY js/ ./js/
COPY views/ ./views/

RUN npm i

ENV LC_ALL=C.UTF-8

ARG PORT=3000
ENV PORT=${PORT}
EXPOSE ${PORT}

HEALTHCHECK --interval=1m --timeout=30s --start-period=1m --retries=10 \
	CMD wget --quiet --tries=1 --spider http://localhost:${PORT} || exit 1

CMD ["node", "app"]
