#
# SQLite Browser
#
# USAGE:
#   docker run -d \
#     --net host \
#     -v /tmp/.X11-unix:/tmp/.X11-unix \
#     -v $HOME/sqlite:/root/sqlite \
#     -e DISPLAY=unix$DISPLAY \
#     --name sqlitebrowser \
#     portiad/sqlitebrowser
#
# USAGE MAC:
#   open -a XQuartz
#   socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
#   docker run -d \
#     --net host \
#     -v ~/sqlite:/root/sqlite \
### Change DISPLAY to equal VirtualBox IP for vboxnet0 ###
#     -e DISPLAY=192.168.##.#:# \
#     --name sqlitebrowser \
#     portiad/sqlitebrowser



FROM ubuntu:latest
MAINTAINER Portia Dean

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
	sqlite3 \
	libsqlite3-dev \
	sqlitebrowser \
	software-properties-common

CMD sqlitebrowser