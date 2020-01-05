
FROM alpine:3.8

# Installs latest Chromium package.
RUN apk update && apk upgrade \
&& echo @edge http://nl.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories \
&& echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories \
&& apk add --no-cache \
bash \
chromium@edge \
chromium-chromedriver@edge \
nss@edge \
&& rm -rf /var/lib/apt/lists/* \
/var/cache/apk/* \
/usr/share/man \
/tmp/*

EXPOSE 9515

ENTRYPOINT ["chromedriver", "--whitelisted-ips"]
