FROM node:10

WORKDIR /usr/src/app

RUN npm install -g bower && \
    npm install -g polymer-cli --unsafe-perm

EXPOSE 8081

CMD ["polymer", "serve", "-H", "0.0.0.0"]