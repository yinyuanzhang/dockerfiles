FROM lsiobase/alpine.python
MAINTAINER rix1337

RUN apk add --no-cache gcc libc-dev python-dev

# Install Requirements
RUN pip install --upgrade pip
RUN pip install bs4 cfscrape docopt feedparser gevent flask lxml python-dateutil requests

# add local files
COPY root/ /

# node.js for cfscrape
RUN apk add nodejs --update-cache --repository http://dl-4.alpinelinux.org/alpine/edge/community/

# Volumes and Ports
VOLUME /config /jd2/folderwatch
EXPOSE 9090
