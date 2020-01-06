FROM pstauffer/python3:latest

MAINTAINER confirm IT solutions, pstauffer

COPY requirements.txt /requirements.txt

RUN addgroup -g 666 cli && \
    adduser -u 666 -G cli -h /home/cli -g "cli User" -s /bin/sh -D cli && \
    pip install --no-cache-dir -r /requirements.txt

USER cli

ENTRYPOINT ["tower-cli"]
