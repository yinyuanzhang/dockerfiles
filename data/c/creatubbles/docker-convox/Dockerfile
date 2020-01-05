FROM docker:18.02.0-ce

RUN apk --no-cache update && \
    apk --no-cache add --update git tar python py-pip py-setuptools ca-certificates curl groff less && \
    pip --no-cache-dir install awscli && \
    rm -rf /var/cache/apk/*

RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

RUN curl -L https://convox.com/cli/linux/convox -o /tmp/convox
RUN mv /tmp/convox /usr/local/bin/convox
RUN chmod 755 /usr/local/bin/convox

COPY squirrel/microservice/bin/ .
