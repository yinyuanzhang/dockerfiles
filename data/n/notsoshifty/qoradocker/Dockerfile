FROM openjdk:8u151-jdk

ENV VERSION="0.26.5"
ENV DHASH="ffebdfd96a6924bfb2e73ec22756fc6b1512651a798918bb2cec0ae7595bdd6e"
ENV DIR_QORA_TOP=/usr/src
ENV DIR_QORA=${DIR_QORA_TOP}/Qora_v${VERSION}/Qora

LABEL version="${VERSION}"

RUN \
  apt-get update && \
  apt-get install -y xvfb x11vnc net-tools vim less && \
  rm -fr /var/lib/apt/lists/*

RUN \
  mkdir ~/.vnc && \
  x11vnc -storepasswd 1234 ~/.vnc/passwd

ENV DISPLAY=:0

RUN \
  cd ${DIR_QORA_TOP} && \
  wget -nv https://github.com/Qoracoin/Qora/releases/download/${VERSION}/Qora_v${VERSION}.zip && \
  echo "$DHASH Qora_v${VERSION}.zip" | sha256sum -c - && \
  unzip -q Qora_v${VERSION}.zip && \
  rm -f Qora_v${VERSION}.zip

WORKDIR ${DIR_QORA}
EXPOSE 5900

