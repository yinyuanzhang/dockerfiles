FROM alpine:latest

RUN wget http://www.sqlite.org/2017/sqlite-autoconf-3170000.tar.gz

RUN tar xvfz sqlite-autoconf-3170000.tar.gz

RUN apk add --update alpine-sdk

RUN ./sqlite-autoconf-3170000/configure --prefix=/usr

RUN make

RUN make install

RUN rm sqlite-autoconf-3170000.tar.gz

CMD sqlite3
