FROM debian:8-slim
LABEL maintainer="Peter Mescalchin <peter@magnetikonline.com>"

ARG ACE_STREAM_VERSION

RUN apt-get update && apt-get upgrade --yes && \
	apt-get install --no-install-recommends --yes \
		curl \
		libpython2.7 \
		net-tools \
		python-apsw \
		python-lxml \
		python-m2crypto \
		python-pkg-resources && \
	# clean up
	apt-get clean && \
	rm --force --recursive /var/lib/apt/lists && \
	# install server
	curl --silent "http://acestream.org/downloads/linux/acestream_${ACE_STREAM_VERSION}_x86_64.tar.gz" | \
		tar --extract --gzip

EXPOSE 6878/tcp

ENTRYPOINT ["/start-engine"]
CMD ["--client-console"]
