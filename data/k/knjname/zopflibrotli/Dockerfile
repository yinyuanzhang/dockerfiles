FROM gcc:9.1.0 as zopfli

WORKDIR /opt
RUN git clone https://github.com/google/zopfli.git zopfli
WORKDIR /opt/zopfli
RUN make
# => /opt/zopfli/zopfli

FROM gcc:9.1.0 as brotli

WORKDIR /opt
RUN git clone https://github.com/google/brotli.git brotli
WORKDIR /opt/brotli
RUN make
# => /opt/brotli/bin/brotli

FROM busybox:1.30.1-glibc

COPY --from=zopfli /opt/zopfli/zopfli /bin/zopfli
COPY --from=brotli /opt/brotli/bin/brotli /bin/brotli
