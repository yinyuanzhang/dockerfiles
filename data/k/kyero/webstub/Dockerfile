FROM node:11.9-alpine
LABEL maintainer "Ivo Jesus <ivo.jesus@kyero.com>"

ENV LANG="C.UTF-8"
RUN npm install -g stubby
WORKDIR /app
EXPOSE 80

CMD ["stubby", "-s", "80", "-d", "stubs.yml"]
