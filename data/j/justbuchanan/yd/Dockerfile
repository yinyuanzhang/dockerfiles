FROM justbuchanan/docker-archlinux
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>

RUN pacman -Sy --noconfirm python

RUN mkdir /www
WORKDIR /www

COPY nebari.jpg index.html ./

EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]
