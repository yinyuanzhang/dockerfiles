FROM golang:1.11-alpine AS build-env

RUN apk update
RUN apk upgrade
RUN apk add --no-cache curl
RUN apk add --no-cache git
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
WORKDIR /go/src/github.com/ilhammhdd/kudaki-user-auth-service/
COPY . /go/src/github.com/ilhammhdd/kudaki-user-auth-service/
RUN dep ensure
RUN go build -o kudaki_user_auth_service_app

FROM alpine

ARG KAFKA_VERSION
ARG KAFKA_BROKERS
ARG QUERY_DB_PATH
ARG QUERY_DB_USERNAME
ARG QUERY_DB_PASSWORD
ARG QUERY_DB_NAME
ARG DB_PATH
ARG DB_USERNAME
ARG DB_PASSWORD
ARG DB_NAME
ARG MAIL
ARG MAIL_PASSWORD
ARG MAIL_HOST
ARG MAIL_PORT
ARG VERIFICATION_PRIVATE_KEY
ARG VERIFICATION_PUBLIC_KEY
ARG GRPC_PORT
ARG GATEWAY_HOST
ARG RESET_PASSWORD_PUBLIC_KEY
ARG RESET_PASSWORD_PRIVATE_KEY
ARG REDISEARCH_SERVER
ARG USER_REPO_SERVICE_GRPC_ADDRESS

ENV KAFKA_VERSION=$KAFKA_VERSION
ENV KAFKA_BROKERS=$KAFKA_BROKERS
ENV QUERY_DB_PATH=$QUERY_DB_PATH
ENV QUERY_DB_USERNAME=$QUERY_DB_USERNAME
ENV QUERY_DB_PASSWORD=$QUERY_DB_PASSWORD
ENV QUERY_DB_NAME=$QUERY_DB_NAME
ENV DB_PATH=$DB_PATH
ENV DB_USERNAME=$DB_USERNAME
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_NAME=$DB_NAME
ENV MAIL=$MAIL
ENV MAIL_PASSWORD=$MAIL_PASSWORD
ENV MAIL_HOST=$MAIL_HOST
ENV VERIFICATION_PRIVATE_KEY=$VERIFICATION_PRIVATE_KEY
ENV VERIFICATION_PUBLIC_KEY=$VERIFICATION_PUBLIC_KEY
ENV GRPC_PORT=$GRPC_PORT
ENV GATEWAY_HOST=$GATEWAY_HOST
ENV RESET_PASSWORD_PUBLIC_KEY=$RESET_PASSWORD_PUBLIC_KEY
ENV RESET_PASSWORD_PRIVATE_KEY=$RESET_PASSWORD_PRIVATE_KEY
ENV MAIL_PORT=$MAIL_PORT
ENV REDISEARCH_SERVER=$REDISEARCH_SERVER
ENV USER_REPO_SERVICE_GRPC_ADDRESS=$USER_REPO_SERVICE_GRPC_ADDRESS

COPY --from=build-env /go/src/github.com/ilhammhdd/kudaki-user-auth-service/kudaki_user_auth_service_app .

RUN mkdir /certs
VOLUME /certs

EXPOSE $GRPC_PORT

ENTRYPOINT ./kudaki_user_auth_service_app