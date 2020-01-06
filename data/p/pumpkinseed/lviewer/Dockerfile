# build stage for client
FROM node:lts-alpine as build-stage-client
WORKDIR /app
COPY ./client .
RUN npm install
RUN npm run build

# build stage for server
FROM golang:1.12.5-alpine3.9 as build-stage-server
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

ENV GO111MODULE on
WORKDIR /go/src/github.com/PumpkinSeed/lviewer
COPY . .

RUN go get -v ./...
RUN go install -v ./...

# production stage
FROM alpine

COPY --from=build-stage-client /app/dist /usr/share/client
COPY --from=build-stage-server /go/bin/lviewer /usr/bin/lviewer

ENV CLIENT_PUBLIC /usr/share/client
EXPOSE 9000

CMD ["lviewer"]