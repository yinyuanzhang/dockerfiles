FROM debian:latest
MAINTAINER Denis Malyshev <proffdns@mail.ru>
#
ENV DEBIAN_FRONTEND noninteractive
#
RUN apt-get update && apt-get install -y --no-install-recommends firefox-esr \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
#
ADD linux-amd64_deb.tgz /tmp/
#
RUN /tmp/linux-amd64_deb/./install.sh
#
ENTRYPOINT ["/usr/bin/firefox-esr"]
