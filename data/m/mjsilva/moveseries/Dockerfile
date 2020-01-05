FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y php unrar transmission-remote-cli curl

ADD ./moveseries /usr/local/bin/moveseries

RUN chmod +x /usr/local/bin/moveseries

CMD ["/usr/local/bin/moveseries"]
