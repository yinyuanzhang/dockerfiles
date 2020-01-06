FROM alpine:3.8
MAINTAINER Thomas Meissner <docker@thomas.meissner.me>

RUN apk update && apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.6.1
ENV GLOBAL_PW NOT_SET

RUN if [[ "$GLOBAL_PW" == "NOT_SET" ]]; then GLOBAL_PW=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c10`;fi
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
	&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
	&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["dockerize"]
CMD ["--help"]
