FROM node:6.10.0-alpine

RUN apk add --update curl python py-pip ca-certificates unzip

RUN pip install --upgrade pip

RUN pip install -U httpie httpie-unixsocket && rm -rf /var/cache/apk/*

VOLUME ["/opt/irpf-online/commander"]

RUN npm i -g typescript ts-node

RUN curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" && \
    chmod +x /usr/local/bin/gosu


COPY ./entrypoint.sh /

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["node"]
