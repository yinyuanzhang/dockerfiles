FROM alpine:latest as build

RUN apk update && apk add bash ca-certificates git openjdk11-jdk && git clone https://github.com/lewish/asciiflow2

WORKDIR /asciiflow2

RUN ./compile.sh


FROM nginx:alpine

COPY --from=build /asciiflow2 /usr/share/nginx/html
