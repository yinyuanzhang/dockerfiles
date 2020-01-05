FROM node:10-alpine

RUN apk -v add --no-cache --update --repository http://dl-3.alpinelinux.org/alpine/edge/testing \
        make \
        gcc \
        g++ \
        libc6-compat \
        vips-dev \
        fftw-dev \
        bash \
        git \
        jq \
        python \
        py-pip \
        groff \
        less \
        mailcap \
        && \
    pip install --upgrade awscli==1.15.52 python-magic && \
    apk -v --purge del py-pip
CMD [ "/bin/bash"]