FROM python:3.6-alpine3.9

WORKDIR /app

ADD . .

RUN apk add bash git ffmpeg

RUN pip3 install pytelegrambotapi
RUN pip3 install --upgrade git+https://github.com/ytdl-org/youtube-dl.git@master


ENTRYPOINT python bot.py