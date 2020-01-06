FROM golang:1.12 AS build
ENV PROJECT flaked
ENV GOPROXY https://goproxy.io
WORKDIR /src/$PROJECT
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go install -a -tags netgo -ldflags=-w

FROM alpine:3.10
COPY --from=build /go/bin/flaked /bin/flaked
CMD [ "/bin/flaked" ]
