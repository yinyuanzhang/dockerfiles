FROM ubuntu:16.04

WORKDIR /

RUN apt update && apt install -y --no-install-recommends --fix-missing \
    cmake \
    g++ \
    make \
    && apt clean -y \
    && rm -rf /var/lib/apt/lists/*

COPY . /ltp

VOLUME /ltp_data

EXPOSE 12345

RUN cd /ltp && ./configure && make -j "$(nproc)" \
	 && mv bin/ltp_server / && mv lib/libdynet.so /usr/lib/ && cd / && rm -fr ltp

CMD ["/ltp_server", "--last-stage", "all"]