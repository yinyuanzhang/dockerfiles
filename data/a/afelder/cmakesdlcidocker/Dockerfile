FROM  debian:buster-slim
LABEL maintainer = "Armin Felder(https://github.com/arminfelder)"

RUN apt-get update \
    && apt-get install build-essential \
    cmake \
    libsdl2-dev \
    libsdl2-ttf-dev \
    libsdl2-mixer-dev -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /build

CMD ["/bin/bash"]
