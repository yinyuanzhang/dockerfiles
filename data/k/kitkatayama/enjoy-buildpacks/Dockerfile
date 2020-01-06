FROM docker:dind

RUN apk add --no-cache git curl

ENV BUILDPACKS_VERSION 0.1.0

RUN mkdir -p /opt \
    && cd /tmp \
    && curl -fsSLO --compressed "https://github.com/buildpack/pack/releases/download/v$BUILDPACKS_VERSION/pack-v$BUILDPACKS_VERSION-linux.tgz" \
    && tar -xf "pack-v$BUILDPACKS_VERSION-linux.tgz" \
    && mv ./pack /opt \
    && ln -s /opt/pack /usr/local/bin/pack \
    && rm pack-v$BUILDPACKS_VERSION-linux.tgz 

CMD [ "/bin/sh" ]