FROM golang:1.13.5 as stage1
LABEL maintainer="Ebbe Elsborg"

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o run cli/main.go
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo api/main.go

WORKDIR /app/implementation
RUN go test

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=stage1 /app/run .
COPY --from=stage1 /app/main .

EXPOSE 8080
CMD ["./main"]
