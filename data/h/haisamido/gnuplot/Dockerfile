FROM alpine:latest
MAINTAINER Haisam Ido "haisam.ido@gmail.com"

# https://hub.docker.com/r/haisamido/gnuplot/

RUN apk add bash

# Gets the latest available gnuplot
RUN apk add gnuplot

# Adds pdfunite
RUN apk add poppler-utils

CMD ["/bin/bash"]
