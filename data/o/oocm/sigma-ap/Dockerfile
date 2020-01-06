# docker build -f Dockerfile-converter -t sigma/converter .
# docker run -it --rm -v /full/path/source:/data/package sigma/converter {FORMAT}
FROM ubuntu:16.04

MAINTAINER bcessa <ben@pixative.com>

RUN \
    apt update && \
    apt install -y gdal-bin unzip

ADD convert.sh /

ENTRYPOINT ["/convert.sh"]