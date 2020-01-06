FROM golang:1.11 as builder

WORKDIR $GOPATH/src/github.com/petechu/suitecrm_custom_api

COPY . .

ENV GO111MODULE=on

RUN go mod download

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /go/bin/go-suitecrm-api cmd/suitecrm_custom_api/main.go

##########################<3 

FROM alpine:latest

ARG APP_ENV="develop"
ARG HOST_NAME="127.0.0.1"
ARG APP_PORT="3000"
ARG DB_USERNAME="root"
ARG DB_PASSWORD
ARG DB_NAME
ARG DB_DRIVER_NAME="mysql"

ENV APP_ENV=${APP_ENV}
ENV HOST_NAME=${HOST_NAME}
ENV APP_PORT=${APP_PORT}
ENV DB_USERNAME=${DB_USERNAME}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_NAME=${DB_NAME}
ENV DB_DRIVER_NAME=${DB_DRIVER_NAME}

RUN apk --no-cache add ca-certificates

WORKDIR /root/

COPY --from=builder /go/bin/go-suitecrm-api .

EXPOSE ${APP_PORT}

CMD [ "./go-suitecrm-api" ]

