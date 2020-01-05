FROM quay.io/apstndb/alpine-node-rails:node-6.1-base

# eventmachine が g++ を要求
# nodejs 6.1.0 指定の意味はある？
# python2 がないと node-gyp がエラー
# tzdata がないと rake db:migrate がエラー
# linux-headers は sys/types.h が必要なもののため
# wercker require bash
RUN apk --no-cache add gcc git g++ imagemagick-dev make musl-dev mysql-dev \
    python linux-headers tzdata bash ca-certificates curl openssl
