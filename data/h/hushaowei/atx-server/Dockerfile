FROM golang:1.11
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN go build

FROM debian:stretch
WORKDIR /root/
COPY --from=0 /app/ .
ENTRYPOINT ./atx-server --port 8000
