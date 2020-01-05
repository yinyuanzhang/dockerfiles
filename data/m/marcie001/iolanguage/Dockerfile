FROM buildpack-deps:jessie

WORKDIR /work
RUN apt-get update && apt-get install cmake libyajl-dev libpython3.4-dev libgmp-dev libmemcached-dev -y && apt-get clean
RUN git clone --branch 2015.11.11 --depth 1 https://github.com/stevedekorte/io.git
WORKDIR io/build
RUN cmake -Wno-dev .. && make install
CMD ["io"]
