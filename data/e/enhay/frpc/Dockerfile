FROM alpine

ENV FRP_MODEL=frpc

COPY ./frp /etc/frp

RUN set -ex \
  && apk add --no-cache --virtual .build-deps openssl \
  && cd /etc/frp \
  && cp frps /usr/bin \
  && cp frpc /usr/bin \
  && chmod +x /usr/bin/frps \
  && chmod +x /usr/bin/frpc \
  && apk del .build-deps 

VOLUME /etc/frp

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "-model=frpc","-config=/etc/frp/frpc.ini" ]
