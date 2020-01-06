FROM debian:8.7
MAINTAINER Sergey Izgiyaev <sergo27@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive \
	DNSDIST_VERSION=1.2.0-1pdns.jessie

RUN apt-get update && apt-get install --no-install-recommends --no-install-suggests -y curl ca-certificates host && \
	curl https://repo.powerdns.com/FD380FBB-pub.asc | apt-key add - && \
	echo "deb [arch=amd64] http://repo.powerdns.com/debian jessie-dnsdist-12 main" > /etc/apt/sources.list.d/pdns-dnsdist.list && \
	apt-get update && apt-get install -y \
	dnsdist=${DNSDIST_VERSION} && \
	apt-get purge curl ca-certificates -y && \
	apt-get autoremove -y -qq && \
	apt-get clean -qq && \
	rm -rf /var/lib/apt/lists/*

STOPSIGNAL SIGTERM

COPY ./entrypoint.sh /bin/
RUN chmod +x /bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]