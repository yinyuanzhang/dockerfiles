FROM alpine:3.6

LABEL maintainer "Backend Team <backend@socialpoint.es>"

ENV AWS_CLI_VERSION=1.15.33
RUN apk -v --update add \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        make \
        curl \
    && pip install --upgrade awscli==$AWS_CLI_VERSION s3cmd==2.0.1 python-magic\
    && apk -v --purge del py-pip \
    && rm /var/cache/apk/*

VOLUME /root/.aws
VOLUME /project

WORKDIR /project

CMD ["aws"]