FROM piotrmaks/cpp

RUN set -ex; \
	apt-get update; \
	apt-get install --yes --no-install-recommends \
		g++-9 \
	; \
	apt-get clean;

ENV CC=gcc-9
ENV CXX=g++-9
