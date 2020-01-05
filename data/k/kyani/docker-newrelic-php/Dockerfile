FROM kyani/modx:latest
MAINTAINER Peter Olds <polds@kyanicorp.com>

# Install New Relic
RUN apt-get update 
RUN apt-get -yqq install wget
RUN apt-get -yqq install python-setuptools
RUN easy_install pip
RUN mkdir -p /opt/newrelic
WORKDIR /opt/newrelic
RUN wget -r -nd --no-parent -Alinux.tar.gz \
	http://download.newrelic.com/php_agent/release/ >/dev/null 2>&1 \
	&& tar -xzf newrelic-php*.tar.gz --strip=1
ENV NR_INSTALL_SILENT true
RUN bash newrelic-install install
WORKDIR /
RUN pip install newrelic-plugin-agent
RUN mkdir -p /var/log/newrelic
RUN mkdir -p /var/run/newrelic