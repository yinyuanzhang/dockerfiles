FROM python:alpine

ENTRYPOINT [ "/usr/bin/entrypoint.sh"  ]

COPY entrypoint.sh /usr/bin/

RUN apk add --no-cache --virtual .buildDeps \
        build-base \
        git \
        libffi-dev \
        openssl-dev \
        shadow \
    && git clone --depth 1 -b stable-2.8 https://github.com/ansible/ansible.git \
    && cd ansible \
    && python setup.py install \
    && cd .. \
    && rm -rf ansible \
    && pip install \
        boto \
        boto3 \
        PyVmomi \
        xmljson \
    && useradd -m ansible \
    && runDeps="$( \
        scanelf --needed --nobanner --format '%n#p' $(find /usr/local/lib/python*/site-packages/ -name '*.so') \
            | tr ',' '\n' \
            | sort -u \
            | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
    )" \
    && apk add --no-cache --virtual .runDeps $runDeps \
    && apk del --no-cache .buildDeps \
    && ln -s /usr/local/bin/python /usr/bin/python

USER ansible
