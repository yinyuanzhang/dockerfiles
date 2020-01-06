FROM tensorflow/tensorflow:1.10.0-devel-gpu-py3

MAINTAINER Byeong0, <byeong0@gmail.com>

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    apt-utils \
    locales \
    tzdata \
    libssl-dev \
    curl \
    vim \
    git \
    libmysqlclient-dev \
	python-opencv && \
	rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL C.UTF-8
ENV TZ=Asia/Seoul

## setting timezone
#RUN echo "tzdata tzdata/Areas select Asia" > timezone.txt
#RUN echo "tzdata tzdata/Zones/Asia select Seoul" >> timezone.txt
#RUN debconf-set-selections timezone.txt
#RUN rm /etc/timezone
#RUN rm /etc/localtime
#RUN dpkg-reconfigure -f noninteractive tzdata

COPY requirements.txt /usr/src/
WORKDIR /usr/src/

#pip install
RUN    pip install --user --upgrade pip==18.1 \
    && pip install -r /usr/src/requirements.txt

