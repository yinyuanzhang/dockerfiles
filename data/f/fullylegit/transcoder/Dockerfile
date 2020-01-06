FROM golang AS build

RUN apt-get update \
    && apt-get install -y \
        libmagic-dev \
    && go get github.com/fullylegit/transcoder/cmd/... \
    && go build -o /server github.com/fullylegit/transcoder/cmd


FROM jrottenberg/ffmpeg:4.2-nvidia

ENTRYPOINT [ "/bin/bash", "-c" ]

CMD [ "/server" ]

RUN apt-get update \
    && apt-get install -y \
        ghostscript \
        libmagic1

COPY --from=build /server /server

USER nobody