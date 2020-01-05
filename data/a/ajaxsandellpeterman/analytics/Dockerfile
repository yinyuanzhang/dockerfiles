FROM alpine:latest

RUN apk add python3 python3-dev cyrus-sasl libsasl cyrus-sasl-dev krb5 curl gcc g++

RUN pip3 install pyhive thrift sasl thrift_sasl

RUN adduser -S analytics

USER analytics