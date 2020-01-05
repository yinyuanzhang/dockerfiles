FROM node
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN apt-get update && apt-get -y install yasm
WORKDIR /opt
RUN wget https://ffmpeg.org/releases/ffmpeg-4.2.1.tar.bz2
RUN tar xvf ffmpeg-4.2.1.tar.bz2
WORKDIR /opt/ffmpeg-4.2.1
RUN ./configure --prefix=/usr/local/ffmpeg
RUN make
RUN make install
WORKDIR /opt
RUN rm -rf /opt/ffmpeg-4.2.1
