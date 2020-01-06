FROM alpine:latest as curl

RUN apk add --no-cache curl
RUN curl -fsSL -o /dbmate https://github.com/amacneil/dbmate/releases/download/v1.4.1/dbmate-linux-amd64 && chmod +x /dbmate

FROM golang:latest

COPY --from=curl /dbmate /usr/local/bin/dbmate

ENTRYPOINT ["/usr/local/bin/dbmate"]