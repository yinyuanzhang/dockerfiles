FROM golang:alpine AS build-env
ADD . /src
RUN cd /src && go build -o caching-estimation-proxy
# Multi-stage!
FROM alpine
WORKDIR /app
COPY --from=build-env /src/caching-estimation-proxy /app/
ENTRYPOINT ./caching-estimation-proxy
