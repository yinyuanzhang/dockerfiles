FROM alpine:3.8 AS builder
RUN apk add --update --no-cache --virtual .build-deps build-base git \
      && git clone https://github.com/google/jsonnet.git \
      && cd jsonnet \
      && make libjsonnet.so \
      && mkdir -p /opt/jsonnet \
      && cp libjsonnet.so /opt/jsonnet/libjsonnet.so \
      && cp include/libjsonnet.h /opt/jsonnet/libjsonnet.h \
      && cd .. \
      && rm -rf jsonnet \
      && apk del --purge .build-deps

FROM ruby:2.5-alpine3.8
COPY --from=builder /opt/jsonnet/libjsonnet.so /usr/local/lib/libjsonnet.so
COPY --from=builder /opt/jsonnet/libjsonnet.h /usr/local/include/libjsonnet.h

ENV HAKO_VERSION=2.8.0

RUN apk --update --no-cache add openssh git zip make docker libstdc++ \
      && apk add --update --no-cache --virtual .build-deps g++ \
      && JSONNET_USE_SYSTEM_LIBRARIES=1 gem install hako -v ${HAKO_VERSION} -N \
      && gem install specific_install -N && gem specific_install https://github.com/moaikids/hako-parameterstore.git -r 8ed6452bd15e24c01b0143de6bccb5bfa86942a4 \
      && apk del --purge .build-deps
