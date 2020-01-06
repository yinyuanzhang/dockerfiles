FROM zenika/alpine-chrome:latest

MAINTAINER walkonthemarz@gmail.com

USER root
COPY ms_fonts /usr/share/fonts/ms
RUN apk add --no-cache curl msttcorefonts-installer fontconfig \
      && apk add wqy-zenhei --update-cache --repository http://nl.alpinelinux.org/alpine/edge/testing --allow-untrusted \
      && chmod 644 /usr/share/fonts/ms/* && chmod 755 /usr/share/fonts/ms \
      && update-ms-fonts \
      && fc-cache -fv

USER chrome
EXPOSE 9222

ENTRYPOINT ["chromium-browser", "--headless", "--disable-gpu", "--disable-software-rasterizer", "--disable-dev-shm-usage", "--remote-debugging-address=0.0.0.0", "--remote-debugging-port=9222", "http://chromium/"]
