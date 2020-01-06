FROM alpine:3.6

ADD cmake-3.9.3.tar.gz /tmp/cmake
RUN apk add --no-cache gcc g++ make
WORKDIR /tmp/cmake/cmake-3.9.3
RUN ./configure && make && make install
RUN rm -Rf /src/cmake
