FROM alpine:3.9

RUN \
  apk add curl && \
  curl -L https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-arm.tar.gz | tar --strip=1 -zxvf - && \
  mkdir /RPi_Cam_Web_Interface && \
  curl -L https://github.com/silvanmelchior/RPi_Cam_Web_Interface/archive/29973ca19c1ea4b5f1d932915184dbd467fce958.tar.gz | tar --strip=1 -C RPi_Cam_Web_Interface -zxvf -

FROM balenalib/rpi-debian:buster-build-20190806

COPY --from=0 /qemu-arm-static /usr/bin

WORKDIR /RPi_Cam_Web_Interface
COPY --from=0 /RPi_Cam_Web_Interface .
COPY config.txt .

RUN apt-get update && ./install.sh q

COPY entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
