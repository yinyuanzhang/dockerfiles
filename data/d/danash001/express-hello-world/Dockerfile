FROM node:dubnium-alpine
EXPOSE 3000
WORKDIR /srv/src
COPY package.json package.json
RUN npm install && \
  npm audit fix
COPY app.js app.js
CMD node app.js
