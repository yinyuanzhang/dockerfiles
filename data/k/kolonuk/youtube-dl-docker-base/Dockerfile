FROM python:slim

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install wget bash cron procps unzip xz-utils mplayer python3 python3-pip -y --no-install-recommends

RUN pip install flask

RUN wget https://johnvansickle.com/ffmpeg/builds/ffmpeg-git-64bit-static.tar.xz -O /root/ffmpeg.tar.xz && \
    mkdir /root/ffmpeg && \
    tar -xf /root/ffmpeg.tar.xz --directory /root/ffmpeg --strip-components=1 && \
    cd /root/ffmpeg && \
    cp ffmpeg ffmpeg-10bit ffprobe qt-faststart /usr/bin && \
    rm -Rf /root/ffmpeg && \
    rm -f /root/ffmpeg.tar.xz

LABEL maintainer="John Wood <john@kolon.co.uk>"
