FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install openjdk-11-jre-headless leiningen curl -y
RUN apt-get install python3-pyqt5.qtwebkit -y
RUN apt-get install wget -y
RUN wget https://download.calibre-ebook.com/3.48.0/calibre-3.48.0-x86_64.txz -O /opt/calibre-3.48.0-x86_64.txz
RUN mkdir -p /opt/calibre/
RUN tar xvf /opt/calibre-3.48.0-x86_64.txz -C /opt/calibre/
RUN /opt/calibre/calibre_postinstall
RUN useradd -s /bin/bash -m -d /home/builder builder
RUN chown -R builder:builder /opt
RUN mkdir -p /usr/src/app
RUN chown -R builder:builder /usr/src/app
USER builder
WORKDIR /usr/src/app
