FROM debian:buster

LABEL maintainer="cnarf@charline"
LABEL description="Debian buster"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get autoremove --purge -y \
&& apt-get update \
&& apt-get upgrade --no-install-recommends -y \
&& apt-get clean \
&& echo "rm -rf /var/lib/apt/lists/*\nrm /root/finalize.sh" > /root/finalize.sh \
&& chmod +x /root/finalize.sh;
