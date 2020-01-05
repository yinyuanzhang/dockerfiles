FROM        ubuntu:18.04

WORKDIR     /tmp/workdir

RUN     apt-get -yqq update && \
        apt-get --no-install-recommends -yqq install poppler-utils libpoppler73 tesseract-ocr ghostscript ocrmypdf && \
        rm -rf /var/lib/apt/lists/*

MAINTAINER  Colin McFadden <mcfa0086@umn.edu>

ADD     shrinkpdf.sh /usr/local/bin/shrinkpdf
RUN     chmod a+x /usr/local/bin/shrinkpdf
ADD     policy.xml  /etc/ImageMagick-6/policy.xml

ENV     LC_ALL=C.UTF-8
ENV     LANG=C.UTF-8
