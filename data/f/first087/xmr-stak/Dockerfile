# Build
FROM debian as builder

COPY . /src/

RUN apt-get update \
  && set -x \
  && apt-get install --no-install-recommends -y \
    build-essential \
    cmake \
    libmicrohttpd-dev \
    libssl-dev \
    libhwloc-dev \
  && cd /src \
  && cmake -DXMR-STAK_COMPILE=generic -DCUDA_ENABLE=OFF -DOpenCL_ENABLE=OFF . \
  && make

# App
FROM debian

RUN apt-get update \
  && apt-get install -y \
    libmicrohttpd-dev \
    libssl-dev \
    libhwloc-dev \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /src/bin /app
ENTRYPOINT ["/app/xmr-stak"]
CMD ["-h"]
