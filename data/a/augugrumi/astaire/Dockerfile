FROM augugrumi/astaire-dockerbuilds:ubuntu18.04 as builder
WORKDIR /tmpbuilding/
COPY . .
RUN builder -DCMAKE_BUILD_TYPE=Release -DJNI=True

FROM ubuntu:18.04
LABEL maintainer="poloniodavide@gmail.com"

RUN apt-get update && apt-get install -y \
    libcurl4 \
    libjsoncpp* \
    openjdk-8-jdk \
    libboost-thread1.65.1 \
    libboost-system1.65.1 && \
    rm -rf /var/lib/apt/lists/*

VOLUME /data/

EXPOSE 8767
EXPOSE 8767/udp

# FIXME this will broke one day
COPY --from=builder /tmpbuilding/build/src/astaire /usr/bin/astaire
COPY ./docker/bootstrap.sh /usr/bin/bootstrap

ENTRYPOINT ["bootstrap"]