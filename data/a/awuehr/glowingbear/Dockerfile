FROM nginx:1-alpine

ENV GLOWINGBEAR_VERSION=0.7.1

RUN \
    apk update && apk upgrade && \
    wget https://github.com/glowing-bear/glowing-bear/archive/$GLOWINGBEAR_VERSION.tar.gz -O - | tar xzf - && \
    mv -f glowing-bear-$GLOWINGBEAR_VERSION/* /usr/share/nginx/html