FROM debian:8.4

MAINTAINER Mohamed Boudra <mohamed@boudra.me>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q \
	&& apt-get install -y -q --no-install-recommends ssh ruby curl ca-certificates python-pip

RUN curl -sSL https://get.docker.com/ | sh
RUN pip install -U awscli docker-compose
