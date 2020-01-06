FROM openjdk:8u181-jre-alpine3.8

# to support finding the host ip on ECS
RUN apk add --update --no-cache \
    curl \
    jq \
    ttf-dejavu

RUN cd ~; curl https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz | tar xvz --strip-components=1
