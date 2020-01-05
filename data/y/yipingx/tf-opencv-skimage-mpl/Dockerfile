FROM fbcotter/docker-tensorflow-opencv:gpu
MAINTAINER Yiping Xie yipingx@kth.se
RUN apt-get update \
	&& apt-get install -y python3-pip \
	&& pip3 install --upgrade pip \
	&& pip install scikit-image \
	&& pip install matplotlib

