FROM golang:alpine

RUN set -x \
    && apk add --no-cache git \
    && go get github.com/bitly/oauth2_proxy

EXPOSE 4180

ENTRYPOINT ["oauth2_proxy","--http-address=0.0.0.0:4180","--email-domain=ovoenergy.com","-upstream"]
CMD ["http://localhost:8080"]
