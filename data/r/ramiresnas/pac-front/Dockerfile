FROM node:latest
LABEL Author="Ramires Moreira"
WORKDIR /home/app
ENV PORT=3031
EXPOSE $PORT
COPY . /home/app
RUN npm install && npm run homologation
# RUN npm install && npm run build
ENTRYPOINT node server.js
