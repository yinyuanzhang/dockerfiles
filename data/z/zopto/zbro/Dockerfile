# # FROM node:6.14.3-alpine
# # # FROM node:8-alpine
# # # FROM alpine:3.5

# # MAINTAINER tvaaali_v2
# # #FROM selenium/node-chrome

# # RUN apk update

# # WORKDIR /
# # RUN apk add --update xvfb dbus xrandr udev alsa-lib
# # ADD /2-apk /apk
# # RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys
# # RUN apk --no-cache --update add /apk/x11vnc-0.9.13-r0.apk

# # ADD 2-ws ws
# # WORKDIR /ws/
# # RUN npm install
# # WORKDIR /

# # ADD 2-start.sh start.sh
# # RUN chmod +x start.sh

# # CMD /start.sh


# # RUN apk add --update openbox

# # #RUN apk add --update chromium ttf-freefont

# # RUN apk update && apk add --no-cache bash \
# #     alsa-lib \
# #     at-spi2-atk \
# #     atk \
# #     cairo \
# #     cups-libs \
# #     dbus-libs \
# #     eudev-libs \
# #     expat \
# #     flac \
# #     gdk-pixbuf \
# #     glib \
# #     libgcc \
# #     libjpeg-turbo \
# #     libpng \
# #     libwebp \
# #     libx11 \
# #     libxcomposite \
# #     libxdamage \
# #     libxext \
# #     libxfixes \
# #     tzdata \
# #     libexif \
# #     udev \
# #     xvfb \
# #     zlib-dev \
# #     chromium \
# #     chromium-chromedriver \
# #     && apk add wqy-zenhei --update-cache --repository http://nl.alpinelinux.org/alpine/edge/testing --allow-untrusted \
# #     && ln -sf /usr/share/zoneinfo/${TZ} /etc/localtime \
# #     && echo ${TZ} > /etc/timezone \
# #     && rm -rf /var/cache/apk/* \
# #     /usr/share/man \
# #     /tmp/*

# # # RUN mkdir -p /data && adduser -D chrome \
# # #     && chown -R chrome:chrome /data
# # # USER chrome



# # # chrome launch flag https://peter.sh/experiments/chromium-command-line-switches/
# # ENTRYPOINT [ "chromium-browser", \
# #   "--headless", "--no-sandbox", "--disable-gpu", \
# #   "--remote-debugging-address=0.0.0.0", \
# #   "--remote-debugging-port=9222", \
# #   "--disable-dev-shm-usage", \
# #   "--window-size=1920,1080", \
# #   # Disable various background network services, including extension updating,
# #   #   safe browsing service, upgrade detector, translate, UMA
# #   "--disable-background-networking", \
# #   # Disable installation of default apps on first run
# #   "--disable-default-apps", \
# #   # Disable all chrome extensions entirely
# #   "--disable-extensions", \
# #   # Disable syncing to a Google account
# #   "--disable-sync", \
# #   # Disable chrome pop-up notifications which cover the page
# #   "--disable-notifications", \
# #   # Disable built-in Google Translate service
# #   "--disable-translate", \
# #   # Hide scrollbars on generated images/PDFs
# #   "--hide-scrollbars", \
# #   # Disable reporting to UMA, but allows for collection
# #   "--metrics-recording-only", \
# #   # Mute audio
# #   "--mute-audio", \
# #   # Skip first run wizards
# #   "--no-first-run", \
# #   # Disable fetching safebrowsing lists, likely redundant due to disable-background-networking
# #   "--safebrowsing-disable-auto-update", \
# #   # set user data path
# #   "--user-data-dir=/data" \
# # ]





# # # RUN apk update --no-cache \
# # #     chromium>75.0.3770.8 \
# # #     chromium-chromedriver>75.0.3770.8

# # RUN adduser -D zopto

# # RUN apk add ca-certificates wget


# # ADD chromium /home/zopto/.config/chromium
# # ADD extensions    /home/zopto/.extensions

# # RUN rm -rf /ws
# # ADD ws ws
# # WORKDIR /ws/
# # RUN npm install
# # WORKDIR /

# # ADD start.sh start.sh
# # RUN chmod +x start.sh

# # ADD start-chrome.sh start-chrome.sh
# # RUN chmod +x start-chrome.sh

# # EXPOSE 10080
# # EXPOSE 10443


# #-----------------------------------ORIGINAL
# #zopto_zalipne
# FROM node:6.14.3-alpine

# #zopto_zbase
# # FROM bantio/bant_alpine

# WORKDIR /
# RUN apk add --update xvfb dbus xrandr udev alsa-lib
# ADD /2-apk /apk
# RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys
# RUN apk --no-cache --update add /apk/x11vnc-0.9.13-r0.apk

# ADD 2-ws ws
# WORKDIR /ws/
# RUN npm install
# WORKDIR /

# ADD 2-start.sh start.sh
# RUN chmod +x start.sh

# CMD /start.sh

# RUN apk update

# RUN apk add --update openbox
# RUN apk add ca-certificates wget

# # RUN apk add --update chromium ttf-freefont

# RUN apk add --update --no-cache \
#     chromium>75.0.3770.8 \
#     chromium-chromedriver>75.0.3770.8\
# 	ttf-freefont


# # # chrome launch flag https://peter.sh/experiments/chromium-command-line-switches/
# # ENTRYPOINT [ "chromium-browser", \
# #   "--headless", "--no-sandbox", "--disable-gpu", \
# #   "--remote-debugging-address=0.0.0.0", \
# #   "--remote-debugging-port=9222", \
# #   "--disable-dev-shm-usage", \
# #   "--window-size=1920,1080", \
# #   # Disable various background network services, including extension updating,
# #   #   safe browsing service, upgrade detector, translate, UMA
# #   "--disable-background-networking", \
# #   # Disable installation of default apps on first run
# #   "--disable-default-apps", \
# #   # Disable all chrome extensions entirely
# #   "--disable-extensions", \
# #   # Disable syncing to a Google account
# #   "--disable-sync", \
# #   # Disable chrome pop-up notifications which cover the page
# #   "--disable-notifications", \
# #   # Disable built-in Google Translate service
# #   "--disable-translate", \
# #   # Hide scrollbars on generated images/PDFs
# #   "--hide-scrollbars", \
# #   # Disable reporting to UMA, but allows for collection
# #   "--metrics-recording-only", \
# #   # Mute audio
# #   "--mute-audio", \
# #   # Skip first run wizards
# #   "--no-first-run", \
# #   # Disable fetching safebrowsing lists, likely redundant due to disable-background-networking
# #   "--safebrowsing-disable-auto-update", \
# #   # set user data path
# #   "--user-data-dir=/data" \
# # ]




# RUN adduser -D zopto

# # EXPOSE 10080
# # EXPOSE 10443



# #zopto_zbro
# # FROM zopto/zbase


# # ADD chromium /home/zopto/.config/chromium
# # ADD extensions    /home/zopto/.extensions

# RUN rm -rf /ws
# ADD ws ws
# WORKDIR /ws/
# RUN npm install
# WORKDIR /

# ADD start.sh start.sh
# RUN chmod +x start.sh

# ADD start-chrome.sh start-chrome.sh
# RUN chmod +x start-chrome.sh

# EXPOSE 10080
# EXPOSE 10443





# # #-----------------------------------ORIGINAL
# # #zopto_zalipne
# # FROM node:6.14.3-alpine

# # #zopto_zbase
# # # FROM bantio/bant_alpine

# # WORKDIR /
# # RUN apk add --update xvfb dbus xrandr udev alsa-lib
# # ADD /2-apk /apk
# # RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys
# # RUN apk --no-cache --update add /apk/x11vnc-0.9.13-r0.apk

# # ADD 2-ws ws
# # WORKDIR /ws/
# # RUN npm install
# # WORKDIR /

# # ADD 2-start.sh start.sh
# # RUN chmod +x start.sh

# # CMD /start.sh

# # RUN apk update

# # RUN apk add --update openbox

# # RUN apk add --update chromium ttf-freefont

# # RUN adduser -D zopto

# # # EXPOSE 10080
# # # EXPOSE 10443



# # #zopto_zbro
# # # FROM zopto/zbase

# # RUN apk update
# # RUN apk add ca-certificates wget

# # ADD chromium /home/zopto/.config/chromium
# # ADD extensions    /home/zopto/.extensions

# # RUN rm -rf /ws
# # ADD ws ws
# # WORKDIR /ws/
# # RUN npm install
# # WORKDIR /

# # ADD start.sh start.sh
# # RUN chmod +x start.sh

# # ADD start-chrome.sh start-chrome.sh
# # RUN chmod +x start-chrome.sh

# # EXPOSE 10080
# # EXPOSE 10443





# #-----------------------------------ORIGINAL
FROM node:6.14.3-alpine
WORKDIR /
RUN apk add --update xvfb dbus xrandr udev alsa-lib
ADD /2-apk /apk
RUN cp /apk/.abuild/-58b83ac3.rsa.pub /etc/apk/keys
RUN apk --no-cache --update add /apk/x11vnc-0.9.13-r0.apk
ADD 2-ws ws
WORKDIR /ws/
RUN npm install
WORKDIR /
ADD 2-start.sh start.sh
RUN chmod +x start.sh
CMD /start.sh
RUN apk update
RUN apk add --update openbox
RUN apk add --update chromium ttf-freefont
RUN adduser -D zopto
RUN apk update
RUN apk add ca-certificates wget
ADD chromium /home/zopto/.config/chromium
ADD extensions    /home/zopto/.extensions
RUN rm -rf /ws
ADD ws ws
WORKDIR /ws/
RUN npm install
WORKDIR /
ADD start.sh start.sh
RUN chmod +x start.sh
ADD start-chrome.sh start-chrome.sh
RUN chmod +x start-chrome.sh
EXPOSE 10080
EXPOSE 10443
