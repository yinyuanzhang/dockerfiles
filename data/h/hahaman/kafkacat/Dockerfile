FROM alpine:3.9

ARG VERSION=1.4.0

RUN apk add --no-cache openssl-dev curl git build-base bash tar wget python yajl yajl-dev cmake coreutils &&\
  git clone --branch ${VERSION} --single-branch https://github.com/edenhill/kafkacat.git kafkacat &&\
  cd kafkacat &&\
  git checkout tags/${VERSION} &&\
  ./bootstrap.sh &&\
  make install &&\
  strip /usr/local/bin/kafkacat

FROM alpine:3.9
MAINTAINER hahaman

ARG BUILD_DATE
ARG SOURCE_COMMIT
ARG DOCKERFILE_PATH
ARG SOURCE_TYPE

# Set timezone to Bangkok
ENV TZ=Asia/Bangkok

# Add timezone data
RUN apk add -U tzdata \
    && cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    # Cleanup
    && rm -rf /var/cache/apk/* && rm -rf /usr/share/zoneinfo

COPY --from=0 /usr/local/bin/kafkacat /usr/local/bin/

CMD ["kafkacat"]