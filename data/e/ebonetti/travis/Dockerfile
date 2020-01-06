FROM ubuntu

RUN set -eux; \
	apt-get update && apt-get install -y \
		ruby-full \
		libxml2-dev \
		git; \
    gem install --no-document travis; \
	apt-get clean; \
	rm -rf /var/lib/apt/lists/*;

ENTRYPOINT ["travis"]