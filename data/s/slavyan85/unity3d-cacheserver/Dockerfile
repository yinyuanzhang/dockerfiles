FROM node:8-alpine
LABEL MAINTAINER="Vyacheslav Kryuchenko <slavyan.85@mail.ru>"

RUN npm install unity-cache-server -g && \
    npm cache clean --force

EXPOSE 8126
VOLUME /data

CMD ["unity-cache-server", "--log-level", "2", "--cache-path", "/data"]