FROM clojure:alpine
MAINTAINER Andre Boechat <boechat107@gmail.com>

# Installing XVFB and Firefox.
# Refs.:
# https://wiki.alpinelinux.org/wiki/Awesome(wm)_Setup
# https://bugs.alpinelinux.org/issues/5694
RUN apk add --no-cache xvfb firefox-esr dbus ttf-freefont && \
        dbus-uuidgen > /var/lib/dbus/machine-id
