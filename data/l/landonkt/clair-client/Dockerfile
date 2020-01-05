FROM alpine:3.8

LABEL Description="Clair Container Scanning" Vendor="Platform Engineering" Version="0.0"

RUN apk add --no-cache \
		ca-certificates git make musl-dev go curl 

# set up nsswitch.conf for Go's "netgo" implementation (which Docker explicitly uses)
# - https://github.com/docker/docker-ce/blob/v17.09.0-ce/components/engine/hack/make.sh#L149
# - https://github.com/golang/go/blob/go1.9.1/src/net/conf.go#L194-L275
# - docker run --rm debian:stretch grep '^hosts:' /etc/nsswitch.conf
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' > /etc/nsswitch.conf

ENV DOCKER_CHANNEL stable
ENV DOCKER_VERSION 18.09.0
# TODO ENV DOCKER_SHA256
# https://github.com/docker/docker-ce/blob/5b073ee2cf564edee5adca05eee574142f7627bb/components/packaging/static/hash_files !!
# (no SHA file artifacts on download.docker.com yet as of 2017-06-07 though)

RUN set -eux; \
	\
# this "case" statement is generated via "update.sh"
	apkArch="$(apk --print-arch)"; \
	case "$apkArch" in \
		x86_64) dockerArch='x86_64' ;; \
		armhf) dockerArch='armel' ;; \
		aarch64) dockerArch='aarch64' ;; \
		ppc64le) dockerArch='ppc64le' ;; \
		s390x) dockerArch='s390x' ;; \
		*) echo >&2 "error: unsupported architecture ($apkArch)"; exit 1 ;;\
	esac; \
	\
	if ! wget -O docker.tgz "https://download.docker.com/linux/static/${DOCKER_CHANNEL}/${dockerArch}/docker-${DOCKER_VERSION}.tgz"; then \
		echo >&2 "error: failed to download 'docker-${DOCKER_VERSION}' from '${DOCKER_CHANNEL}' for '${dockerArch}'"; \
		exit 1; \
	fi; \
	\
	tar --extract \
		--file docker.tgz \
		--strip-components 1 \
		--directory /usr/local/bin/ \
	; \
	rm docker.tgz; \
	\
	dockerd --version; \
	docker --version

# COPY modprobe.sh /usr/local/bin/modprobe
# COPY docker-entrypoint.sh /usr/local/bin/

#Go
ENV GOVERSION 1.10.7
RUN mkdir /goroot && mkdir -p /gopath/src && mkdir -p /gopath/bin && mkdir -p /gopath/pkg
RUN curl https://storage.googleapis.com/golang/go${GOVERSION}.linux-amd64.tar.gz \
           | tar xvzf - -C /goroot --strip-components=1

#set ENV
ENV GOPATH /gopath
ENV GOROOT /goroot
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH

#Get Dep
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh

#Clone the Clair Scanner
WORKDIR /gopath/src/
RUN git clone https://github.com/arminc/clair-scanner.git
WORKDIR /gopath/src/clair-scanner
RUN make ensure && \
	make build && \
	mv clair-scanner /clair-scanner && \
	rm -rf /gopath/src/clair-scanner
WORKDIR /

CMD ["sh","-c","./clair-scanner --ip localhost -c ${CLAIR_URL} ${SCAN}"]
