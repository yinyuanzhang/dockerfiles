FROM golang:alpine

ARG app_env
ENV APP_ENV $app_env

RUN apk add --update tzdata \
    bash wget curl git \
    && curl https://glide.sh/get | sh;

WORKDIR /go/src/ibabysite/api
COPY ./api /go/src/ibabysite/api

RUN glide install \
    && go build

CMD if [ ${APP_ENV} = development ]; \
    then \
    go get github.com/pilu/fresh \
    && fresh; \
    fi

EXPOSE 3000