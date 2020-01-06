FROM alpine:latest

RUN apk update && \
    apk add curl py-pip && \
    pip install --upgrade pip && \
    rm -rf /var/cache/apk/*

ADD requirements.txt /usr/local/src/requirements.txt

RUN pip install --upgrade -r /usr/local/src/requirements.txt

ENTRYPOINT [ "/entrypoint.sh" ]

ADD /entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
