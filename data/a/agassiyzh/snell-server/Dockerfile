FROM ubuntu

WORKDIR /app

RUN apt-get update &&\
    apt-get install -y  unzip wget &&\
    wget -O snell-server.zip https://github.com/surge-networks/snell/releases/download/v1.1.1/snell-server-v1.1.1-linux-amd64.zip && \
    unzip snell-server.zip 

COPY snell-server.conf /app/snell-server.conf
COPY entrypoint.sh /app/entrypoint.sh


ENTRYPOINT [ "/bin/bash", "entrypoint.sh" ]
