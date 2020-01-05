# Start from base node alpine image
FROM node:10-alpine

# install imagemagick, graphicsmagick, ffmgeg and
RUN apk add --no-cache imagemagick ffmpeg graphicsmagick

# install bash
RUN apk add --no-cache bash

# try fix
RUN ln -s /bin/sh /bin/source

ENTRYPOINT ["/bin/sh", "-c"]
