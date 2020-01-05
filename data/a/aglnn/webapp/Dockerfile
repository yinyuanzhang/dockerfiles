FROM golang:alpine as build
RUN mkdir /src
COPY src/web.go /src
WORKDIR /src
RUN go build /src/web.go
CMD ["/src/web"]
EXPOSE 8080

FROM alpine:latest as production
RUN mkdir /web
COPY --from=build /src/web  /web/
CMD ["/web/web"]
