FROM ubuntu:18.10 AS builder

ADD . /build

RUN apt update && \
    apt install -y cmake gcc g++ git libexpat-dev libboost-system-dev libboost-program-options-dev libboost-thread-dev libboost-filesystem-dev libboost-regex-dev libboost-test-dev zlib1g-dev libssl-dev

RUN mkdir -p /build/build /app && cd /build/build && \
    cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. && make librethinkdb_lib &&  make dehancer_xmp_cpplib install && make


FROM ubuntu:18.10

WORKDIR /app

RUN apt update && \
    apt install -y openssl expat && \
    apt-get clean autoclean && \
    rm -rf /var/lib/{apt,dpkg,cache,log}/

COPY --from=builder /build/build/services/lic-generator/licensed /app/licensed
COPY --from=builder /build/build/services/mlutd/dehancer-mlutd /app/dehancer-mlutd
COPY --from=builder /build/build/services/backend/dehancerd /app/dehancerd
COPY --from=builder /build/services/etc /app/etc

CMD [""]
