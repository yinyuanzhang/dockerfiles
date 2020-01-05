FROM alpine:3
RUN apk add --no-cache npm && \
    delgroup ping && \
    addgroup -g 999 drone && \
    adduser -G drone -D -H -h /drone/src -u 999 drone && \
    npm i -g @antora/cli@2.0 @antora/site-generator-default@2.0
