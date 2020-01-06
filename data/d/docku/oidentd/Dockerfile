FROM docku/base
MAINTAINER Jon Chen <docku@burrito.sh>

EXPOSE 113

RUN pacman -Syu --noconfirm --needed oidentd
ADD oidentd_run /service/oidentd/run
