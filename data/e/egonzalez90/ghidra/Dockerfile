FROM openjdk:11-slim

RUN apt update \
    && apt install -y wget \
                      bsdtar \
                      libxrender1 \
                      libxtst6 \
                      libxi6 \
                      libxext6 \
                      libfreetype6 \
                      libfontconfig1 \
                      zip \
    && apt clean all

ENV DISPLAY :0
VOLUME /tmp/.X11-unix:/tmp/.X11-unix
WORKDIR /ghidra

ENV GHIDRA_RELEASE ghidra_9.1_PUBLIC_20191023
RUN wget https://ghidra-sre.org/$GHIDRA_RELEASE.zip \
    && bsdtar --strip-components=1 -xvf $GHIDRA_RELEASE.zip \
    && chmod +x ./ghidraRun \
    && rm -rf $GHIDRA_RELEASE.zip

CMD ./support/ghidraDebug