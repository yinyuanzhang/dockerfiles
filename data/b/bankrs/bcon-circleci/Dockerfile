FROM golang:1.11.4-stretch
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils=1.4.8 ca-certificates=20161130+nmu1+deb9u1 curl=7.52.1-5+deb9u8 make=4.1-9.1 git=1:2.11.0-3+deb9u4 ssh=1:7.4p1-10+deb9u4 apt-transport-https=1.4.8 software-properties-common=0.96.20.2-1 python-wheel=0.29.0-2 python-pip=9.0.1-2 python-setuptools=33.1.1-1 gnupg=2.1.18-8~deb9u3 \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN curl -fsSL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends docker-ce=5:18.09.0~3-0~debian-stretch nodejs=11.5.0-1nodesource1 \
  && npm install -g --no-progress junit-merge@2.0.0 && npm cache clean --force \
  && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade awscli==1.16.75
RUN curl -fsSL "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN go get -u golang.org/x/lint/golint
RUN go get -u honnef.co/go/tools/cmd/megacheck
RUN go get -u github.com/gordonklaus/ineffassign
RUN go get -u github.com/remyoudompheng/go-misc/deadcode
RUN go get -u github.com/client9/misspell/cmd/misspell
RUN go get -u github.com/mdempsky/unconvert
RUN go get -u github.com/jgautheron/goconst
RUN go get -u github.com/ribice/glice
RUN go get -u github.com/mgechev/revive
RUN go get -u github.com/kevinburke/go-bindata/go-bindata
RUN go get -u golang.org/x/tools/cmd/stringer
ADD https://github.com/hadolint/hadolint/releases/download/v1.15.0/hadolint-Linux-x86_64 /usr/local/bin/hadolint
RUN chmod u+x /usr/local/bin/hadolint

CMD ["/bin/bash"]
