FROM ubuntu:18.04

MAINTAINER Anush

# ---------------------------
# --- Install required tools

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
	apt-get install -y \
		curl \
		git \
		expect \
		wget \
		zip \
		unzip \
		nodejs \
		npm \
		chromium-browser

RUN apt-get clean

