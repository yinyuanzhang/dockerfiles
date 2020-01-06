FROM burbon/common:0.1

ENV GOLANG_VERSION 1.13.1

RUN goRelArch='linux-amd64'; \
        goRelSha256='94f874037b82ea5353f4061e543681a0e79657f787437974214629af8407d124'; \
        url="https://dl.google.com/go/go${GOLANG_VERSION}.${goRelArch}.tar.gz"; \
        wget -O go.tgz "$url"; \
        echo "${goRelSha256} *go.tgz" | sha256sum -c -; \
        tar -C /usr/local -xzf go.tgz; \
	    rm go.tgz; \
        export PATH="/usr/local/go/bin:$PATH"; \
        go version

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 755 "$GOPATH"
WORKDIR $GOPATH
