FROM jimmycuadra/rust:latest

RUN \
	apt-get update && \
	apt-get upgrade -y && \
	apt-get install -y curl gnupg && \
	curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
	apt-get install -y npm

RUN npm install -g codecov

RUN mkdir /ci
WORKDIR /ci

RUN rustup install nightly && \
	rustup default nightly

ENTRYPOINT [ "/bin/bash" ]
