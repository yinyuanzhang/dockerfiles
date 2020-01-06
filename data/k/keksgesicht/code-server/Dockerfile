FROM keksgesicht/code-server

RUN set -x \
&&	apt-get update \
&&	apt-get install -y --no-install-recommends --no-install-suggests \
		python3 python3-pip \
&&	apt-get clean autoclean \
&&	apt-get autoremove -y \
&&	rm -rf /var/lib/apt/lists/*
