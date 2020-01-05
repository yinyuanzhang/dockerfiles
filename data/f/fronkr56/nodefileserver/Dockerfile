FROM node:alpine
RUN npm update npm -g && npm install http-server -g
EXPOSE 80
ENTRYPOINT http-server /exposed -p 80
