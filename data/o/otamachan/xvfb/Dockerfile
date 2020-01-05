FROM ubuntu:trusty
RUN apt-get update \
    && apt-get install -y --no-install-recommends xvfb libgl1-mesa-dri \
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
ENV DISPLAY :1
COPY start.sh /
VOLUME /tmp/.X11-unix
ENTRYPOINT ["/start.sh"]
