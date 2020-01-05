FROM debian:stretch-slim

LABEL "de.andrelademann"="André Lademann" \
	version="0.0.4" \
	description="Docker debian image to use for development, testing and deployment."

RUN apt-get update &&\
    apt-get install -y \
			bats \
			curl \
			figlet \
			findutils \
			git \
			make \
			mc \
			siege \
			wget \
			vim \
			zip
