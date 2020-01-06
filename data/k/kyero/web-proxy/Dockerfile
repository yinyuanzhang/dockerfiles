FROM heroku/heroku:16

LABEL maintainer "Ivo Jesus <ivo.jesus@kyero.com>"

ENV LANG="C.UTF-8" \
    PORT="80"

EXPOSE ${PORT}

RUN mkdir /app

COPY ./dist/bin/ /app/bin/
COPY ./dist/config/ /app/config/

WORKDIR /app

CMD ["bin/start-nginx"]
