FROM golang:alpine AS build

WORKDIR /app

COPY ./main.go /app/
RUN go build main.go

FROM alpine:latest
EXPOSE 8080

COPY --from=build /app/main /

CMD /main
