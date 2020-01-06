FROM alpine

WORKDIR /opt
COPY . /opt

RUN apk add --update --no-cache --quiet python git openjdk8-jre bash \
  && ./compile.sh \
  && apk del --quiet openjdk8-jre curl bash git \
  && rm -rf asciiflow2-master closure-compiler.jar compile.sh /var/cache .git/

FROM nginx:alpine
COPY --from=0 /opt /usr/share/nginx/html
