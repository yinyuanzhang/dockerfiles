FROM bash
LABEL maintainer="Seti <sebastian.koehlmeier@kyberna.com>"

RUN apk --no-cache add openssh-client curl rsync && \
    ln -s $(which bash) /bin/bash