# Pull base image.
FROM ubuntu:bionic

RUN apt-get update && apt-get install -y \
  vim \
  curl \
  git \
  golang-go \
  software-properties-common \
  && rm -r /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs && rm -r /var/lib/apt/lists/*

RUN add-apt-repository ppa:canonical-chromium-builds/stage

RUN apt-get update && apt-get install -y \
  chromium-browser  \
  jq \
  && rm -r /var/lib/apt/lists/*

RUN npm install -g selenium-side-runner lighthouse html-validator-cli broken-link-checker

RUN go get github.com/ericchiang/pup
RUN export GOROOT=/usr/bin/go
RUN ln -s ~/go/bin/pup /usr/bin/pup

# Set correct entrypoint
CMD ["/bin/bash"]
ENTRYPOINT []
