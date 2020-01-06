FROM golang:1.7.3-alpine

RUN apk add --update-cache build-base musl-dev musl-utils tar sudo

RUN wget http://www.musl-libc.org/releases/musl-1.1.10.tar.gz && tar -xvf musl-1.1.10.tar.gz && cd musl-1.1.10 && ./configure && make && sudo make install && cd .. && rm musl-1.1.10.tar.gz && rm -Rf musl-1.1.10 && rm -Rf musl.1.1.10 && rm -Rf musl.1.1.10

RUN rm -rf /var/cache/apk/*


