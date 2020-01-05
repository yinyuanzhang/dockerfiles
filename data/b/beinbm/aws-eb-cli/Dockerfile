FROM alpine:3.6
RUN apk -v --no-cache add \
        git \
        less \
        openssh-client \
        py-pip \
        python \
        zip \
        && \
    pip install --upgrade awsebcli awscli
    
VOLUME /app
WORKDIR /app
