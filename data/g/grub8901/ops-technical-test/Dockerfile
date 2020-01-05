#

FROM golang:1.13-alpine AS build

WORKDIR /build

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o simpleserver .

FROM alpine:3.10 AS serve

ARG GITSHA

WORKDIR /srv

COPY --from=build /build/simpleserver ./

RUN echo "${GITSHA}" > GITSHA

EXPOSE 8080

CMD ["/srv/simpleserver"]
