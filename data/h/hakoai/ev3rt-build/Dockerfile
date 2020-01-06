FROM sharaku/ev3rt-build
MAINTAINER hakoai

ENV EV3RT_LIB_NAME=ev3rt-beta7-2-release \
    EV3RT_LIB_PATH=/var/lib/ev3rt

ENV EV3RT_WORKSPACE=${EV3RT_LIB_PATH}/hrp2/sdk/workspace

RUN \
  wget --no-check-certificate http://www.toppers.jp/download.cgi/${EV3RT_LIB_NAME}.zip -P /tmp/ && \
  unzip /tmp/${EV3RT_LIB_NAME}.zip -d /tmp && \
  mv /tmp/${EV3RT_LIB_NAME} ${EV3RT_LIB_PATH} && \
  cd ${EV3RT_LIB_PATH} && \
  tar Jxvf hrp2.tar.xz && \
  rm hrp2.tar.xz && \
  cd hrp2/cfg && \
  make

COPY build.sh ${EV3RT_WORKSPACE}
