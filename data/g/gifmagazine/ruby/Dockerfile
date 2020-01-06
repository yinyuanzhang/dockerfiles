FROM ruby:2.6.3-alpine

RUN apk update \
    && apk upgrade \
    && apk add --no-cache \
        bash \
        curl \
        ffmpeg \
        file \
        g++ \
        gifsicle \
        git \
        imagemagick6 \
        less \
        linux-headers \
        make \
        mysql-dev \
        nodejs \
        python \
        tzdata \
    && ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && rm -rf /usr/mysql-test \
    && rm -f /usr/lib/libmysqld* \
    && curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl \
    && chmod a+rx /usr/local/bin/youtube-dl \
    && ln -s /usr/bin/convert-6 /usr/local/bin/convert \
    && ln -s /usr/bin/ffmpeg /usr/local/bin/ffmpeg \
    && ln -s /usr/bin/ffprobe /usr/local/bin/ffprobe \
    && ln -s /usr/bin/gifsicle /usr/local/bin/gifsicle \
    && ln -s /usr/bin/identify-6 /usr/local/bin/identify
