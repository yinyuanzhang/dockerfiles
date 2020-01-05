FROM python:3-alpine

LABEL maintainer "eric@daras.family"

RUN apk add gcc ffmpeg musl-dev --no-cache \
	&& pip install 'streamlink<=1.2.0'  \
	&& apk del gcc musl-dev --no-cache \
	&& rm -Rf /tmp/*
EXPOSE 8080
ENTRYPOINT ["streamlink", \
	"--player-external-http", \
	"--player-external-http-port", "8080" \
]
