FROM docker/whalesay:latest

RUN apt update -y && apt install -y fortunes

CMD /usr/games/fortune | tr a-z A-Z | cowsay
