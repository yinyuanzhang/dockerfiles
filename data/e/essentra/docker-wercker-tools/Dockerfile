FROM ubuntu:18.04

RUN apt-get -qqy update \
	&& apt-get -qqy --no-install-recommends install \
	software-properties-common \
	jq \
	openssh-client \
	curl \
	bzip2 \
	unzip \
	wget \
	git \
	nano \
	python3-pip \
	python3-dev \
	python3-setuptools \
	netcat \
	net-tools \
	libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev \
	ruby-full && \
	rm -rf /var/lib/apt/lists/* /var/cache/apt/* 

RUN python3 -m pip -q install --upgrade pip \
    && python3 -m pip -q install requests azure-storage-blob locustio requests