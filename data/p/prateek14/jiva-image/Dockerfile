FROM ubuntu:16.04
MAINTAINER prateek14 <prateek.pandey@cloudbyte.com>
RUN apt-get update && apt-get install -y \
             git \
	     automake \
	     gcc \
	     curl \
	     make \
	     apt-transport-https \
	     ca-certificates \
	     && rm -rf /var/lib/apt/lists/*
	     
ENV GOLANG_VERSION 1.7.3
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 508028aac0654e993564b6e2014bf2d4a9751e3b286661b0b0040046cf18028e

RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
	&& echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
	&& tar -xzf golang.tar.gz -C /usr/local \
        && rm golang.tar.gz
	
RUN mkdir -p /go
ENV GOPATH=/go
ENV PATH $PATH:/usr/local/go/bin/:$GOPATH/bin

#adding docker group
RUN groupadd -r docker
#usermod -aG docker $USER && \
RUN useradd --create-home --gid docker unprivilegeduser

# Go tools
RUN go get github.com/rancher/trash
RUN go get github.com/golang/lint/golint

# Install longhorn Docker driver
RUN GOPATH=/tmp/docker-longhorn-driver && \
    mkdir -p $GOPATH/src/github.com/rancher && \
    cd $GOPATH/src/github.com/rancher && \
    git clone https://github.com/rancher/docker-longhorn-driver.git && \
    cd docker-longhorn-driver && \
    git checkout ea7bf49977adb179a2d767f8a5dcf3ec380a34a2 && \
    go build -o /usr/local/bin/docker-longhorn-driver

# Docker
RUN curl -sL https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 > /usr/bin/docker && \
chmod +x /usr/bin/docker

#Docker install
#apt-get update ;\
#apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D ;\
#echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee /etc/apt/sources.list.d/docker.list ;\
#apt-get update ;\
#apt-cache policy docker-engine ;\
#apt-get install -y docker-engine
#Run env | grep DOCKER && \
#echo "done" && \
#systemctl status docker && \
#service docker status ;\
#docker info



RUN mkdir -p $GOPATH/src/github.com/openebs/
RUN cd $GOPATH/src/github.com/openebs/ && \
    git clone https://github.com/openebs/longhorn.git && \
    cd $GOPATH/src/github.com/openebs/longhorn && \
    trash . && \
    ls -ltr scripts/ && \
    chmod -R 777 scripts/ && \
    ls -ltr scripts/ && \
    make -k
ENTRYPOINT ["./scripts/entry"]
CMD ["ci"]
