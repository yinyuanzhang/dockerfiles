FROM bash:5
RUN apk -v --update add \
        findutils \
        zip \
        unzip \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        && \
    pip install --upgrade awscli==1.16.89 s3cmd==2.0.2 python-magic && \
    apk -v --purge del py-pip && \
    rm /var/cache/apk/*
VOLUME /root/.aws
VOLUME /project
WORKDIR /project
