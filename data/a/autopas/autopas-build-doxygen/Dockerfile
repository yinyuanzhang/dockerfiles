FROM autopas/build-base:latest

# install doxygen
RUN true \
	&& apt-get -qq update \
	&& apt-get -qq install -y --no-install-recommends \
		doxygen \
		graphviz \
	&& rm -rf /var/lib/apt/lists/*

CMD ["sh", "-c", "cmake ../.. >/dev/null && echo \"\ndoxygen warnings:\" && make doc_doxygen > /dev/null"]
