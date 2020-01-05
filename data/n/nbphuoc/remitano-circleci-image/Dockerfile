FROM circleci/ruby:2.5.3
LABEL description="Ruby + Node + Chrome + Haproxy"
LABEL version="2.5.3"
MAINTAINER Phuoc Nguyen <ba.phuoc.nbp@gmail.com>

RUN echo deb http://httpredir.debian.org/debian stretch-backports main | sudo tee /etc/apt/sources.list.d/backports.list
RUN curl https://haproxy.debian.net/bernat.debian.org.gpg | sudo apt-key add -
RUN echo deb http://haproxy.debian.net stretch-backports-1.8 main | sudo tee /etc/apt/sources.list.d/haproxy.list
RUN sudo apt-get update; true
RUN sudo apt-get install -y haproxy
RUN sudo apt-get install -y lsof ffmpeg
RUN sudo apt-get install -y xclip
RUN sudo apt-get install -y vim tmux
RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
		g++ \
		gcc \
		libc6-dev \
		make \
		pkg-config

ENV GOLANG_VERSION "1.12.6"
ENV GOLANG_ARCH "linux-amd64"

RUN set -eux; \
	url="https://golang.org/dl/go${GOLANG_VERSION}.${GOLANG_ARCH}.tar.gz"; \
	sudo wget -O go.tgz "$url"; \
	sudo tar -C /usr/local -xzf go.tgz; \
	sudo rm go.tgz; \
	export PATH="/usr/local/go/bin:$PATH"; \
	go version

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN sudo mkdir -p "$GOPATH/src" "$GOPATH/bin" && sudo chmod -R 777 "$GOPATH"

RUN go get github.com/prasmussen/gdrive

ENV CURRENT_CHROME_VERSION=69.0.3497.92
RUN curl --silent --show-error --location --fail --retry 3 --output /tmp/google-chrome-stable_current_amd64.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
      && (sudo dpkg -i /tmp/google-chrome-stable_current_amd64.deb || sudo apt-get -fy install)  \
      && rm -rf /tmp/google-chrome-stable_current_amd64.deb \
      && sudo sed -i 's|HERE/chrome"|HERE/chrome" --disable-setuid-sandbox --no-sandbox|g' \
           "/opt/google/chrome/google-chrome" \
      && google-chrome --version
RUN curl -sL https://deb.nodesource.com/setup_9.x | sudo bash
RUN sudo apt-get install nodejs
RUN sudo npm install -g yarn
