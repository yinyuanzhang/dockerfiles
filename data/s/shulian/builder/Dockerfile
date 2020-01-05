FROM alpine:edge

RUN mkdir -p /go
ENV GOPATH=/go
ENV PATH=$GOPATH/bin:$PATH

RUN apk add --no-cache python3 python3-dev go npm docker git build-base protobuf
RUN pip3 install --no-cache-dir setuptools wheel Cython flake8 coverage twine setuptools_scm pysocks
RUN go get -u golang.org/x/lint/golint
