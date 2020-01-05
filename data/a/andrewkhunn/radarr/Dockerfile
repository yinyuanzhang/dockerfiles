FROM hotio/radarr
LABEL maintainer="andrewkhunn"

RUN apt-get update && \
    apt-get install -y python-pip python-setuptools ffmpeg && \
    pip --no-cache-dir install requests requests[security] requests-cache babelfish "guessit<2" "subliminal<2" && \
    pip uninstall -y stevedore && \
    pip --no-cache-dir install stevedore==1.19.1 python-dateutil deluge-client qtfaststart && \
    apt-get clean && \
    rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*
