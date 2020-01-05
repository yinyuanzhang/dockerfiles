FROM alpine
LABEL maintainer="arturkv82"
RUN apk add --update nodejs nodejs-npm
COPY . /
WORKDIR /
RUN npm install
EXPOSE 8080
ENTRYPOINT [ "npm", "run", "start"]