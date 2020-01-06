FROM ubuntu:bionic

# MAINTAINER Gábor Somogyi
MAINTAINER Larry Cai

RUN apt-get update && apt-get install -y wget python xz-utils xdg-utils \
    pandoc imagemagick && \
    apt-get clean

RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.py | python -c "import sys; main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read()); main()"

WORKDIR /ebook

# ENTRYPOINT ["ebook-convert"]
