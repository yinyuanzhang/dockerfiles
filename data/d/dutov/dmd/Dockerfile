FROM debian:8.5
MAINTAINER Anton Dutov <anton.dutov@gmail.com>
RUN echo "deb http://master.dl.sourceforge.net/project/d-apt/ d-apt main" > /etc/apt/sources.list.d/d-apt.list
RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install -y --allow-unauthenticated --reinstall d-apt-keyring
RUN apt-get update
RUN apt-get install -y --no-install-recommends dmd-bin dub build-essential
RUN apt-get install -y --no-install-recommends openssh-client


