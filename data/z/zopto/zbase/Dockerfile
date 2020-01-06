FROM zopto/zalpine

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

RUN apk add --update openbox

RUN apk add --update chromium ttf-freefont

RUN adduser -D zopto

EXPOSE 10080
EXPOSE 10443
