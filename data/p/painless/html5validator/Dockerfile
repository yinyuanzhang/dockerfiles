FROM python:3-slim

# NOTE: We need to do an mkdir as long the openjdk package is broken 8-/

RUN mkdir -p /usr/share/man/man1 \
 && apt-get update \
 && apt-get install -y openjdk-11-jre-headless \
 && apt-get clean

RUN pip3 install html5validator

WORKDIR /app

USER nobody

CMD ["html5validator", "--root", "/app", "--also-check-css", "--show-warnings"]
