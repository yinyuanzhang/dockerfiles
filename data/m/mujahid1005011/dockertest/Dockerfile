FROM docker/whalesay:latest
RUN apt-get -y update && apt-get install -y fortunes
RUN apt-get install -y apache2
CMD /usr/games/fortune -a | cowsay
