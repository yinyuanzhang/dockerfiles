FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
	apt-transport-https \
	ca-certificates \
	git \
	curl \
	gnupg \
	libnss3 \
	libnss3-tools \
	libfontconfig1 \
	xvfb \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update && apt-get install -y \
	google-chrome-stable 

RUN Xvfb :10 -screen 0 1280x720x16 &

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get install -y nodejs

RUN npm install -g ember-cli
WORKDIR /usr/src/