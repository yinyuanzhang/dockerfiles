FROM debian:wheezy
RUN echo deb http://archive.debian.org/debian wheezy main > /etc/apt/sources.list && \
echo deb http://archive.debian.org/debian-security wheezy/updates main >> /etc/apt/sources.list && \
echo 'Acquire::Check-Valid-Until "0";' > /etc/apt/apt.conf.d/debian-eol
