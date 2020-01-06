FROM ubuntu:latest
MAINTAINER Mao Jianwei <maojianwei2020@gmail.com>

RUN apt-get update \
    && apt-get install -y vlc \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -M mao

EXPOSE 5511

CMD ["su", "mao", "-c", "cvlc /home/maoMedia --repeat --sout '#rtp{sdp=rtsp://:5511/}' --sout-keep --quiet"]
