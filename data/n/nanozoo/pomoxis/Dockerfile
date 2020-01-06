FROM ubuntu:xenial
ENV VERSION v0.2.2

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN	apt-get install -y \
			libatlas-base-dev \
			libbz2-dev \
			libffi-dev \
			libhdf5-dev \
			liblzma-dev \
			libncurses5-dev \
			libopenblas-base \
			libopenblas-dev \
			zlib1g-dev \
			make \
			python3-all-dev \
			virtualenv \
			wget \
			bzip2 \
			cmake \
			gcc-4.9 \
			git \
			g++-4.9

RUN apt-get clean all && \
		apt-get purge && \
		rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV CXX="g++-4.9" CC="gcc-4.9"

RUN mkdir /ONT && \
	cd /ONT && \
	git clone --branch $VERSION --recursive https://github.com/nanoporetech/pomoxis && \
	cd pomoxis && \
	make install

ENV PATH /ONT/pomoxis/venv/bin/:$PATH
