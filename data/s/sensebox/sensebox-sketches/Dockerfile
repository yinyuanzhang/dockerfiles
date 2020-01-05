FROM debian:9.4-slim as builder

ENV IDE_VERSION=1.8.5 \
  SENSEBOXCORE_VERSION=1.3.1 \
  ARDUINO_SAMD_VERSION=1.6.21 \
  ARDUINO_AVR_VERSION=1.6.21 \
  SENSEBOXCORE_URL=https://raw.githubusercontent.com/sensebox/senseBoxMCU-core/master/package_sensebox_index.json \
  SENSEBOX_LIBRARY_URL=https://github.com/sensebox/senseBox_library/archive/master.zip \
  TELEGRAM_LIBRARY_URL=https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot/archive/v1.1.0.zip \
  ARDUINO_JSON_LIBRARY_URL=https://github.com/bblanchon/ArduinoJson/releases/download/v5.13.5/ArduinoJson-v5.13.5.zip \
  PATH=$PATH:/arduino-ide

RUN apt-get update && apt-get install -y xz-utils unzip wget \
  && wget http://downloads.arduino.cc/arduino-$IDE_VERSION-linux64.tar.xz \
  && tar xf arduino-$IDE_VERSION-linux64.tar.xz \
  && mv arduino-$IDE_VERSION /arduino-ide \
  && wget -O senseBox_Library.zip $SENSEBOX_LIBRARY_URL \
  && unzip senseBox_Library.zip -d /arduino-ide/libraries \
  && wget -O telegram_Library.zip $TELEGRAM_LIBRARY_URL \
  && unzip telegram_Library.zip -d /arduino-ide/libraries \
  && wget -O arduino_json_Library.zip $ARDUINO_JSON_LIBRARY_URL \
  && unzip arduino_json_Library.zip -d /arduino-ide/libraries \
  && arduino --pref boardsmanager.additional.urls=$SENSEBOXCORE_URL --install-boards sensebox:samd:$SENSEBOXCORE_VERSION \
  && arduino --install-boards arduino:samd:$ARDUINO_SAMD_VERSION \
  && arduino --install-boards arduino:avr:$ARDUINO_AVR_VERSION \
  && mkdir -p /arduino-ide/build-cache \
  && mv /root/.arduino15/packages /arduino-ide/packages \
  && apt-get purge -y xz-utils unzip wget \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf arduino-$IDE_VERSION-linux64.tar.xz senseBox_Library.zip /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && bash -c 'rm -rf /arduino-ide/{java,lib,reference,examples,arduino,install.sh,revisions.txt,uninstall.sh}' \
  && find /arduino-ide -type d -name "examples" -exec rm -rf \;

FROM node:8-slim

WORKDIR /app

ENV NODE_ENV=production

COPY package.json /app
COPY yarn.lock /app

RUN yarn install --pure-lockfile --production

COPY src /app/src
COPY --from=builder /arduino-ide /app/src/arduino-ide

CMD ["yarn","start"]
