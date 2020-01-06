############################################################
# TCSJOHNHUXLEY Docker Image Build and Test Image          #
############################################################
FROM tcsjh/dockerenv:1.0
LABEL maintainer="jessica.mowatt@tcsjohnhuxley.com"
USER root
RUN set -x && \
	export DEBIAN_FRONTEND=noninteractive && \
	apt-get update && \
	apt-get install -y --no-install-recommends python \
		curl && \
        apt autoremove -y && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists
USER builder
