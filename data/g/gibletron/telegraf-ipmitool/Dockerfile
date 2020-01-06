FROM telegraf:latest

MAINTAINER giblet

RUN apt-get update && \
    apt-get install -yq \
    ipmitool && \
# Cleanup
    apt-get clean && \
    rm -rf \
	/tmp/* \
	/var/lib/apt/lists/* \
	/var/tmp/*

# CMD ["telegraf"]
