FROM node:8.9.4-alpine
RUN apk add --update curl bash \
  && rm -rf /var/cache/apk/* \
  && curl -L https://download.docker.com/linux/static/stable/x86_64/docker-17.03.0-ce.tgz > /docker.tgz && \
    cd / && \
    tar -xvzf /docker.tgz && \
    mv /docker/* /usr/local/bin && \
    rm /docker.tgz
