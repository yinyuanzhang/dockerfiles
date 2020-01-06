FROM gliderlabs/alpine:latest

MAINTAINER Andrey Gulitskiy <wyorma@gmail.com>

# Upgrade system
RUN apk upgrade

# Install stuff
RUN apk-install bash tzdata git wget curl

# Set timezone
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime && \
	echo "UTC" > /etc/timezone

