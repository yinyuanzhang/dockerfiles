FROM debian:stretch-slim

RUN set -x \
    && apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y git ca-certificates automake gcc libc-dev make \
    && git clone https://github.com/multiplay/qstat.git \
    && cd qstat \
    && ./autogen.sh \
    && ./configure \
    && make \
    && make install \
    && apt-get remove --purge --auto-remove -y git ca-certificates automake gcc libc-dev make \
    && rm -rf /var/lib/apt/lists/*

CMD ["qstat"]