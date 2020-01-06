FROM ubuntu:16.04 as builder

LABEL maintainer Mario Werner <mario.werner@iaik.tugraz.at>

RUN apt-get update && apt-get install -y \
  autoconf \
  bison \
  build-essential \
  file \
  git \
  gperf \
  help2man

RUN git clone https://github.com/niosHD/veriwell.git /tmp/veriwell && \
    cd /tmp/veriwell && \
    ./configure --prefix=/opt/veriwell && \
    make install

FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    scons && \
  pip3 install pytest pytest-xdist

COPY --from=builder /opt/veriwell /opt/veriwell
RUN ln -s /opt/veriwell/bin/veriwell /usr/local/bin/veriwell
