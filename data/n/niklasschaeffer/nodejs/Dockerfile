FROM debian:jessie

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get upgrade -y \
	curl \
	wget \
	git \
	build-essential

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash

RUN apt-get update && apt-get upgrade -y \
	nodejs	

RUN npm i npm@latest -g

RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

WORKDIR /var/www
