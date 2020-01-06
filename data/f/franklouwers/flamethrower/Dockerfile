FROM ubuntu:disco as build
# Needs very recent version of libuv!

RUN apt-get update && apt-get install -y cmake build-essential g++ libuv1-dev libldns-dev libgnutls28-dev pkg-config
WORKDIR /app
ADD https://github.com/DNS-OARC/flamethrower/archive/v0.9.tar.gz .
RUN tar zxvf v0.9.tar.gz
WORKDIR flamethrower-0.9/build
RUN cmake .. && make

FROM ubuntu:disco as prod
LABEL maintainer="frank@louwers.be"
LABEL github.url="https://github.com/franklouwers/flamethrower-docker"

RUN apt-get update && apt-get install -y libuv1 libldns2 libssl1.1 libstdc++6
COPY --from=build /app/flamethrower-0.9/build/flame /usr/local/bin/flame
ENTRYPOINT ["/usr/local/bin/flame"]
CMD ["--help"]
