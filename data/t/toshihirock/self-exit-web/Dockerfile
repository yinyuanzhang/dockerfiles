#FROM alpine
FROM node:10-alpine3.9

#RUN apk add nodejs nodejs-npm nodejs-current
# Bundle app source
COPY . .
EXPOSE 80
ENTRYPOINT node app.js
