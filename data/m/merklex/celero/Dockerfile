FROM ubuntu:bionic

RUN apt-get update && \
  apt-get install -y build-essential cmake git wget unzip libncurses5-dev && \
  rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/DigitalInBlue/Celero/archive/v2.3.0.zip
RUN unzip v2.3.0.zip && \
  cd Celero-2.3.0 && \
  mkdir -p build && \
  cd build && \
  cmake .. && \
  make install
