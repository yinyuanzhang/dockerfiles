FROM node:6.11.3
MAINTAINER Matt Gibney <matt@nodeten.co.uk>

# install chrome for default testem config (as of 2.15.0)
RUN apt-get update &&\
    apt-get install -y \
        apt-transport-https \
        gnupg \
        --no-install-recommends &&\
	curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - &&\
	echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list &&\
	apt-get update &&\
	apt-get install -y \
	    google-chrome-stable \
	    --no-install-recommends

# tweak chrome to run with --no-sandbox option
RUN \
	sed -i 's/"$@"/--no-sandbox "$@"/g' /opt/google/chrome/google-chrome

# Install ember-cli
RUN \
	npm install -g ember-cli@2.15.1
