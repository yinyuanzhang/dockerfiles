FROM prima/nginx:1.12.2-3

# TZ: https://github.com/primait/board/issues/1631
ENV TZ=:/etc/localtime

RUN rm /etc/nginx/conf.d/default.conf
COPY files/pyxis.conf /etc/nginx/conf.d/pyxis.conf
COPY files/entrypoint.sh /entrypoint.sh

WORKDIR /code

ENTRYPOINT ["/entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
