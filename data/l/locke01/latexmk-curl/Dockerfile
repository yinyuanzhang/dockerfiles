FROM tianon/latex

MAINTAINER locke01

RUN apt-get update && apt-get install -y curl && \
	apt-get autoclean && apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*