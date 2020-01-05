FROM zenika/alpine-chrome:77
LABEL maintainer="eiriksm <eirik@nymedia.no>"
USER root
RUN mkdir -p mkdir /var/cache/apk \
        && apk add --update chromium-chromedriver --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community

ENTRYPOINT ["chromedriver",  "--port=8643", "--url-base=wd/hub", "--headless", "--no-sandbox", "--whitelisted-ips="]
EXPOSE 8643

