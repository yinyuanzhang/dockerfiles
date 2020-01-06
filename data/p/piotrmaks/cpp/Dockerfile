FROM ubuntu:19.04

RUN set -ex; \
	apt-get update && \
	apt-get install --yes --no-install-recommends \
		python3-pip \
		git \
		make \
	&& \
	pip3 install setuptools && \
	pip3 install --no-cache-dir cmake conan && \
	apt-get clean && \
	mkdir -p /tmp/build;

ENV CONAN_USER_HOME=/tmp
