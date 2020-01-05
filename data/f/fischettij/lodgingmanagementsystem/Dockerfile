FROM node:10-alpine as builder

WORKDIR /app

RUN apk add git
RUN git clone https://github.com/fischettij/lodgingManagementSystem .
RUN npm install --production


FROM node:10-alpine

WORKDIR /app

COPY --from=builder \
        /app/*.js \
        /app/api \
        /app/node_modules \
        ./

EXPOSE 3000
CMD ["node","server.js"]
