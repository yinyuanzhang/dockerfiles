FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget
RUN wget https://github.com/Automattic/simplenote-electron/releases/download/v1.0.8/Simplenote-linux-x64.1.0.8.tar.gz
RUN tar -xzvf Simplenote-linux-x64.1.0.8.tar.gz
RUN apt-get install -y libgtk2.0-0
RUN apt-get install -y libxtst6
RUN apt-get install -y libxss1
RUN apt-get install -y gconf2
RUN apt-get install -y libnss3
RUN apt-get install -y libasound2
RUN apt-get install -y libcanberra-gtk-module libcanberra-gtk3-module
ENTRYPOINT /Simplenote-linux-x64/Simplenote
