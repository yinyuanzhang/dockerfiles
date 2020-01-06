# Always use a specific jenkins version, never use 'latest'
FROM alpine:3.8
LABEL Description="Cloudreach Internal Jenkins Build Server Helper"
RUN apk -v --update add \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        && \
    pip install --upgrade awscli==1.15.70 s3cmd==2.0.1 python-magic jinja2-cli pyyaml && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*
