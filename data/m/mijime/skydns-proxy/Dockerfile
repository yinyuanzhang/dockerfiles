FROM nginx:1.9

ENV VERSION 0.10.0

ADD https://github.com/kelseyhightower/confd/releases/download/v${VERSION}/confd-${VERSION}-linux-amd64 /usr/bin/confd

RUN chmod +x /usr/bin/confd

ADD etc/confd /etc/confd

ENTRYPOINT [ "/entrypoint.sh" ]

ADD entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
