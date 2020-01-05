FROM node:10

WORKDIR /usr/src/app
COPY . .

RUN npm install && npm run build && npm -g install serve
CMD ["serve", "-s", "build", "-l", "80"]

EXPOSE 80
