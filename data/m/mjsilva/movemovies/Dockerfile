FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y unrar rsync curl

ADD ./movemovies /usr/local/bin/movemovies

RUN chmod +x /usr/local/bin/movemovies

CMD ["/usr/local/bin/movemovies"]
