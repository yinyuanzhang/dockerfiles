FROM python:3-alpine

RUN apk add --no-cache ffmpeg
RUN pip install --no-cache-dir r128gain

CMD [ "r128gain", "-r", "-a", "-s", "/music" ]
