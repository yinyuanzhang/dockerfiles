FROM openjdk:8-jre

ENV SDKMAN_DIR /usr/local/sdkman

RUN set -x \
    && apt-get update \
    && apt-get install -y zip --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN curl -s get.sdkman.io | bash

RUN mkdir -p $SDKMAN_DIR/etc

RUN set -x \
    && echo "sdkman_auto_answer=true" > $SDKMAN_DIR/etc/config \
    && echo "sdkman_auto_selfupdate=false" >> $SDKMAN_DIR/etc/config \
    && echo "sdkman_insecure_ssl=false" >> $SDKMAN_DIR/etc/config

COPY init-sdkman.sh /init-sdkman.sh
RUN bash -c 'source /init-sdkman.sh'
