FROM nginx:alpine

RUN apk add --no-cache curl

HEALTHCHECK CMD /usr/bin/curl --fail http://localhost:80 || exit 1
