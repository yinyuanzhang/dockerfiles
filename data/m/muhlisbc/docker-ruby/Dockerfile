FROM ruby:2.3

MAINTAINER Muhlis BC "muhlisbc@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN buildDeps=' \
	ca-certificates \
	nginx-full \
	nodejs \
	' \
	&& apt-get update \
	&& apt-get install --no-install-recommends --no-install-suggests -y $buildDeps \
	&& gem install bundler --no-doc --no-ri \
	&& rm -rf /var/lib/apt/lists/* /tmp/* \
