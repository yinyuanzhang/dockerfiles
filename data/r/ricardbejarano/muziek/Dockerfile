FROM python:3-alpine

COPY --chown=100:100 . /opt/muziek

RUN apk add --no-cache --virtual .build-dependencies gcc musl-dev linux-headers && \
    pip install --no-cache-dir -r /opt/muziek/requirements.txt && \
    apk del .build-dependencies && \
    apk add --no-cache ffmpeg && \
    echo "nogroup:*:100:nobody" > /etc/group && \
    echo "nobody:*:100:100:::" > /etc/passwd && \
    mkdir /library && \
    chown 100:100 /library

USER 100:100
WORKDIR /opt/muziek
VOLUME ["/library"]
EXPOSE 3000/tcp
ENTRYPOINT ["uwsgi", "--enable-threads", "--wsgi-file", "/opt/muziek/server.py"]
CMD ["--http", "0.0.0.0:3000"]
