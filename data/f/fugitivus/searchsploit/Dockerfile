#debian container for general purpose and teaching students:
#build with docker build -f debian.docker -t fugitivus/debian:latest .

FROM debian:latest
MAINTAINER fugitivus <benjamin.altenhoener@gmx.de>

#environment-variables for non-interactive shell:
#ENV DEBIAN_FRONTEND noninteractive

#install updates, some packages and do cleanup:
RUN apt-get update && apt-get upgrade -y\
 && apt-get install apt-utils git make -y\
 && apt-get install net-tools htop bmon joe aptitude -y\
 && git clone https://github.com/offensive-security/exploit-database.git\
# && ./exploit-database/searchsploit --update\
 && apt-get clean autoclean\
 && apt-get autoremove -y\
 && rm -rf /var/lib/{apt,dpkg,cache,log}/
