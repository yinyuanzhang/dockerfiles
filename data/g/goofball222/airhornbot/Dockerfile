FROM golang:alpine

LABEL \
    org.label-schema.vendor="The Goofball - goofball222@gmail.com" \
    org.label-schema.url="https://github.com/goofball222/airhornbot" \
    org.label-schema.name="Discord Airhorn Bot" \
    org.label-schema.version=$VERSION \
    org.label-schema.vcs-url="https://github.com/goofball222/airhornbot.git" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.license="MIT" \
    org.label-schema.schema-version="1.0"

WORKDIR /opt/airhornbot

COPY . .

RUN \
    apk add -q --no-cache --virtual .build-deps \
        gcc git musl-dev \
    && go mod vendor \
    && go build cmd/bot/bot.go \
    && apk del -q --purge .build-deps \
    && rm -rf /tmp/* /var/cache/apk/*

CMD ["./bot", "-t YOUR_TOKEN_HERE"]
