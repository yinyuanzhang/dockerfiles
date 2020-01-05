FROM openjdk:8-jre-alpine

LABEL maintainer="Thomas"

ENV BURP_COMMUNITY_VERSION 1.7.36

RUN apk --no-cache add ca-certificates \
                       ttf-dejavu \
    && adduser -D -h /tester tester \
    && wget -O /tester/burp.jar "https://portswigger.net/burp/releases/download?product=community&version=$BURP_COMMUNITY_VERSION&type=jar" \
    && chown -R tester /tester

USER tester

WORKDIR /tester

ENTRYPOINT [ "java", "-jar", "burp.jar" ]
