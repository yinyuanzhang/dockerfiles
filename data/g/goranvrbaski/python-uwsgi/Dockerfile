FROM alpine:latest

LABEL maintainer="vrbaski.goran@gmail.com"

RUN apk add --update --no-cache \
    python3 \
    uwsgi \
    uwsgi-python3 && \
    pip3 install --upgrade pip && \
    find / -type d -name __pycache__ -exec rm -r {} +   && \
    rm -rf /usr/lib/python*/ensurepip                   && \
    rm -rf /usr/lib/python*/turtledemo                  && \
    rm -rf /usr/lib/python*/idlelib                     && \
    rm -f /usr/lib/python*/turtle.py                    && \
    rm -f /usr/lib/python*/webbrowser.py                && \
    rm -f /usr/lib/python*/doctest.py                   && \
    rm -f /usr/lib/python*/pydoc.py                     && \
    rm -rf /root/.cache /var/cache

