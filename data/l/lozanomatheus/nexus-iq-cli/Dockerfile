FROM alpine:3.9.4

WORKDIR /opt/

ENV GOROOT="/usr/lib/go" \
    GOPATH="/go" \
    PATH="/go/bin:$PATH"

RUN mkdir -p ${GOPATH}/src ${GOPATH}/bin \
    && apk add --no-cache openjdk8 python3 curl npm nodejs git make musl-dev go \
    && curl -L https://bootstrap.pypa.io/get-pip.py | python3

RUN curl -LO https://download.sonatype.com/clm/scanner/nexus-iq-cli-1.64.0-02.jar

CMD [ "java", "-jar", "/opt/nexus-iq-cli-1.64.0-02.jar" ]
