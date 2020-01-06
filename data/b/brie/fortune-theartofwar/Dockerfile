FROM ubuntu:latest

RUN apt-get -y update && apt-get -y upgrade && apt-get -y install fortune-mod
COPY The_Art_Of_War* /usr/share/games/fortunes/

ENTRYPOINT ["/usr/games/fortune", "/usr/share/games/fortunes/The_Art_Of_War"]
