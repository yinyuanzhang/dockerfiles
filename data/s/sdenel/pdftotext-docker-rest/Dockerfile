FROM alpine:latest
# Adapted from: https://github.com/frol/docker-alpine-python3/blob/master/Dockerfile
RUN apk add --no-cache poppler-utils python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools flask && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY webserver.py /webserver.py

CMD ["/webserver.py"]