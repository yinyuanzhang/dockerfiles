FROM golang
ADD ./src /go/src
ADD ./public_html /go/public_html

RUN go get github.com/aws/aws-sdk-go/aws
RUN go get github.com/aws/aws-sdk-go/service/s3
RUN go get github.com/aws/aws-sdk-go/aws/session
RUN go get github.com/aws/aws-sdk-go/service/s3/s3manager
RUN go get github.com/aws/aws-sdk-go/service/cloudfront
RUN go get github.com/gorilla/mux

RUN go install main

WORKDIR /go