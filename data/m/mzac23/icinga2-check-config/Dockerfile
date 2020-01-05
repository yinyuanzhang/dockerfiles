FROM debian:latest

MAINTAINER Zachary McGibbon

# Install required packages to install Icinga2
RUN export DEBIAN_FRONTEND=noninteractive \
	&& apt-get update \
	&& apt-get --quiet install --yes curl gnupg lsb-release

# Install Icinga2
RUN export DEBIAN_FRONTEND=noninteractive \
	&& curl -s https://packages.icinga.com/icinga.key | apt-key add - \
	&& echo "deb http://packages.icinga.org/debian icinga-$(lsb_release -cs) main" > /etc/apt/sources.list.d/icinga2.list \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends icinga2
