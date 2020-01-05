FROM golang:stretch as tools-build

ARG OPERATOR_SDK_VERSION=v0.5.0

RUN go get -u github.com/golang/dep/cmd/dep && \
    go get -u github.com/derekparker/delve/cmd/dlv && \
    go get -u github.com/cespare/reflex && \
    go get -u github.com/mgechev/revive && \
    mkdir -p $GOPATH/src/github.com/operator-framework && \
    cd $GOPATH/src/github.com/operator-framework && \
    git clone https://github.com/operator-framework/operator-sdk && \
    cd operator-sdk && \
    git checkout tags/${OPERATOR_SDK_VERSION} && \
    make dep && \
    make install

FROM golang:stretch

ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="operator-debug-bastion" \
      org.label-schema.description="Bastion container that is able to compile and run Kubernetes operators" \
      org.label-schema.url="https://github.com/kns-it/docker-docfx" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/baez90/operator-debug-bastion" \
      org.label-schema.vendor="Baez" \
      org.label-schema.version="0.0.1" \
      org.label-schema.schema-version="1.0" \
      maintainer="peter.kurfer@gmail.com"

COPY --from=tools-build /go/bin /go/bin

RUN curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/bin/kubectl && \
    chmod +x /usr/bin/kubectl

ADD sleep.sh /

EXPOSE 2345

ENTRYPOINT [ "/bin/bash" ]
CMD ["/sleep.sh"]