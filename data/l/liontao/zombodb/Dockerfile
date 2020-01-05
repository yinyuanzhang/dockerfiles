FROM postgres:10-alpine

LABEL maintainer="taojiachun31@foxmail.com"

RUN apk add --no-cache git make gcc g++ curl-dev

RUN git clone --depth 1 https://github.com/zombodb/zombodb.git && cd zombodb &&  make install &&  cd .. &&  rm -rf zombodb 

RUN apk del git make gcc g++

EXPOSE 5432

CMD ["postgres"]
