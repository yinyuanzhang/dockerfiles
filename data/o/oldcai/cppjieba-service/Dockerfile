FROM alpine:latest
#RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
RUN apk --no-cache add cmake clang clang-dev make gcc g++ libc-dev linux-headers
WORKDIR /code/

RUN wget https://github.com/yanyiwu/cppjieba/archive/master.zip && \
    unzip master.zip && rm -f master.zip && mv cppjieba-master cppjieba && \
    wget https://github.com/oldcai/cppjieba-server/archive/master.zip && \
    unzip master.zip && rm -f master.zip && mv cppjieba-server-master cppjieba-server

RUN cd cppjieba && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_EXE_LINKER_FLAGS="-static" .. && \
    make && \
    cd /code/cppjieba-server && \
    mkdir build && \
    cd build && \
    cmake -D CMAKE_EXE_LINKER_FLAGS="-static" .. && \
    make

FROM alpine:latest
COPY --from=0 /code/cppjieba-server/dict /run/dict/
COPY --from=0 /code/cppjieba-server/build/bin/cjserver /run/cppjieba-server
COPY config.conf /run/config.conf
WORKDIR /run/
CMD ["/run/cppjieba-server", "./config.conf"]

EXPOSE 80
