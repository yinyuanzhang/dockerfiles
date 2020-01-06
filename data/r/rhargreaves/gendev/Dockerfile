FROM ubuntu:18.04
WORKDIR /tmp
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
	apt-get install -y \
	build-essential wget unzip \
	unrar-free texinfo \
	git openjdk-8-jre-headless && \
	apt-get clean
RUN mkdir gendev
COPY . gendev/
RUN bash -c "cd gendev && make && rm -rf /tmp/*"
CMD /bin/bash
