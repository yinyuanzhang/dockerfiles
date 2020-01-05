FROM python:3.6-alpine

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN echo "http://dl-cdn.alpinelinux.org/alpine/latest-stable/community" >> /etc/apk/repositories && \
    apk add --no-cache docker && \
    pip3 install --no-cache-dir docker-compose && \
    pip3 install --no-cache-dir -r requirements.txt

COPY composesentry ./composesentry
CMD [ "python", "-m", "composesentry", "--config", "/config"]
