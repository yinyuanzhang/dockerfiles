FROM python:2.7
MAINTAINER mickare <info@mickare.de>

RUN apt-get update && apt-get install -y \
	python-pip \
	python-dev \
	python3 \
	python3-pip \
	gcc \
	&& rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install --upgrade pip \
	&& pip --no-cache-dir install --upgrade \
		coverage \
		nose

RUN pip3 --no-cache-dir install mypy

#RUN useradd -ms /bin/bash runner
#USER runner
#WORKDIR /home/runner
