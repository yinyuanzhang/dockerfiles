FROM codenvy/ubuntu_android

# --- Golang ---

RUN sudo apt-get update && sudo apt-get install -y --no-install-recommends \
    g++ \
    gcc \
    libc6-dev \
    make \
    && sudo rm -rf /var/lib/apt/lists/*

ENV GOLANG_VERSION 1.7.4
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 47fda42e46b4c3ec93fa5d4d4cc6a748aa3f9411a2a2b7e08e3a6d80d753ec8b

RUN sudo curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
    && echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
    && sudo tar -C /usr/local -xzf golang.tar.gz \
    && sudo rm golang.tar.gz

RUN sudo sed -i '$ d' /home/user/.bashrc
ENV GOPATH /projects/go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN sudo mkdir -p "$GOPATH/src" "$GOPATH/bin" && sudo chmod -R 777 "$GOPATH"

EXPOSE 8080 5001

# --- Node ---

ENV NODE_VERSION=0.12.9 
ENV NODE_PATH=/usr/local/lib/node_modules

RUN sudo apt-get update && \
    sudo apt-get -y install build-essential libssl-dev libkrb5-dev gcc make ruby-full rubygems-integration python && \
    sudo gem install sass compass && \
    sudo apt-get clean && \
    sudo apt-get -y autoremove && \
    sudo apt-get -y clean && \
    sudo rm -rf /var/lib/apt/lists/* && \
    set -ex \
    && for key in \
      9554F04D7259F04124DE6B476D5A82AC7E37093B \
      94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
      0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
      FD3A5288F042B6850C66B31F09FE44734EB7990E \
      71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
      DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
    ; do \
      gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
    done && \
  	cd /home/user && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
  	&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  	&& gpg --verify SHASUMS256.txt.asc \
  	&& grep "node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
  	&& sudo tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
  	&& sudo rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc
	
EXPOSE 3000 5000 9000
RUN sudo npm install -g npm@latest
RUN sudo npm install --unsafe-perm -g gulp bower grunt grunt-cli yeoman-generator yo generator-angular generator-karma generator-webapp

CMD tail -f /dev/null
