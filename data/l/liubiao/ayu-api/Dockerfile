FROM golang:1.12 AS builder

ENV GO111MODULE=on

WORKDIR /app

COPY go.mod .
COPY go.sum .

RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -ldflags="-s -w" -o ayu
#RUN GOOS=linux GOARCH=amd64 go build -v -o /app/ayu-dashboard/sso-server


FROM alpine

WORKDIR /app

COPY --from=builder /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /app/ayu .
COPY --from=builder /app/config/conf.yaml ./config/conf.yaml
COPY --from=builder /app/docs/swagger.json ./docs/ayu.json

#EXPOSE 8080
CMD [ "/app/ayu" ]