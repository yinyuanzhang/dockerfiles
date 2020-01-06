FROM alpine:3.10

MAINTAINER Andreas Leicher <andreas@kotaico.de>

ENV AWSCLI_VERSION "1.16.214"
ENV HADOLINT_VERSION "1.17.1"

# install aws cli
RUN apk add --update --no-cache \
        bash \
        curl \
        docker \
        git \
        groff \
        less \
        make \
        openssh \
        py-pip \
        python
RUN pip install awscli
RUN apk --purge -v del py-pip
RUN rm -rf /var/cache/apk/*

RUN curl -sL https://github.com/hadolint/hadolint/releases/download/v${HADOLINT_VERSION}/hadolint-Linux-x86_64 > /usr/local/bin/hadolint
RUN chmod a+x /usr/local/bin/hadolint


