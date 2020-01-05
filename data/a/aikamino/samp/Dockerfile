FROM debian:8
LABEL maintainer="kamino <kamino@imea.me>"
WORKDIR /app
EXPOSE 7777/udp

ENV RCON_PASSWORD=password

ADD env/sources.list /etc/apt/sources.list
ADD app/. .

RUN \
    apt update &&\
    apt install -y lib32stdc++6 &&\
    tar -zxvf samp*.tar.gz

CMD ["start-server.sh"]
ENTRYPOINT ["sh"]