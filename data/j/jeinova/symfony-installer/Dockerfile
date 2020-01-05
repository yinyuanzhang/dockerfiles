FROM php:alpine

LABEL maintainer="jeinova"

RUN apk --no-cache add curl

ADD entrypoint.sh entrypoint.sh
RUN chmod +x entrypoint.sh

WORKDIR "/app"

ENTRYPOINT ["/entrypoint.sh"]
CMD ["symfony"]
